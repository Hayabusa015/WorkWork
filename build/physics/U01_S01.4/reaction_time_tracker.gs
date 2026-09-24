/**
 * SHULL PHYSICS — U01/S01.4 Reaction Time Lab
 * Class Data & Dashboard — build script
 *
 * WHAT THIS DOES
 * Run buildReactionTimeTracker() once, in this spreadsheet, and it builds two tabs:
 *   - Data       : one row per student per situation. Left open for anyone who can
 *                  edit this file (Matt, 2026-09-24: shared editable to anyone with
 *                  a school account — set that sharing from the Share button; this
 *                  script cannot set domain-wide link sharing itself).
 *   - Dashboard  : aggregate-only view — this year's class averages, an A/B/C
 *                  comparison chart, and a year-over-year trend. No student names
 *                  appear here by design (Matt, 2026-09-24).
 *
 * WHAT IT DOES NOT DO
 * No network calls, no email, no access outside this one spreadsheet. Reads and
 * writes only within the file it is bound to. Safe to read top to bottom before
 * running it.
 *
 * SET THE YEAR EACH FALL — BEFORE THE FIRST PERIOD RUNS THE LAB
 * Dashboard!B1 is the single "Current School Year" cell. The moment a Data row
 * gets its Situation filled in, the onEdit_ trigger below snapshots B1's value
 * into that row's School Year column as a literal — then never touches that
 * row again, even after B1 changes. Never type a year into the Data tab by
 * hand, and never edit an already-filled School Year cell by hand either.
 * Change B1 once, at the very start of each year, before the first class
 * enters data — a row entered before you update B1 snapshots the OLD year.
 *
 * TO RE-RUN
 * Extensions > Apps Script > run buildReactionTimeTracker, or use the
 * "SHULL Tools > Rebuild Tracker" menu this script adds to the spreadsheet.
 * Re-running is safe — it reuses the existing tabs, rebuilds formulas/validation/
 * charts, and never deletes a row of data already entered.
 *
 * HOW THE REACTION TIME IS COMPUTED
 * Matches the lab's own method exactly (SHULL_PHYS_Lab_U01_S01.4_Reaction_Time,
 * key verified 2026-09-22): t = sqrt(2 * (average drop distance in m) / 9.80).
 * Plain 4-drop average — no automatic outlier exclusion. A bad drop is a
 * judgment call the lab's own post-lab error analysis asks students to make;
 * this sheet does not make that call for them by silently dropping a value.
 *
 * WHERE THIS LIVES
 * Filed flat in the Section 01.4 Drive folder, matching where the lab PDF/DOCX
 * already sit (no Labs-Case Studies-Projects subfolder exists for this section).
 * This is a placement call, not a locked convention — see the delivery note.
 */

const TRACKER_DATA_SHEET = 'Data';
const TRACKER_DASHBOARD_SHEET = 'Dashboard';
const TRACKER_LAST_ROW = 1000; // formulas and validation are pre-filled this far down
const TRACKER_ACCENT = '#896107';   // Physics primaryDeep, brand/tokens.json
const TRACKER_ACCENT_B = '#F5B82E'; // Physics display gold, chart series only

function onOpen() {
  SpreadsheetApp.getUi()
    .createMenu('SHULL Tools')
    .addItem('Rebuild Tracker', 'buildReactionTimeTracker')
    .addToUi();
}

/**
 * Simple trigger — fires automatically on any edit to this spreadsheet by
 * anyone who can edit it (students included; simple triggers run with the
 * editing user's own permissions, which is all this needs).
 *
 * Its only job: the first time a Data row gets a Situation value (col D)
 * AND its School Year cell (col A) is still blank, write Dashboard!B1's
 * CURRENT value into col A as a literal — a snapshot of the year that row
 * was entered in. A row that already has a Year is never touched again,
 * so changing B1 next fall cannot retroactively relabel old rows.
 *
 * Handles multi-cell and multi-row paste, not just single-cell typing.
 */
function onEdit(e) {
  if (!e || !e.range) return;
  const sheet = e.range.getSheet();
  if (sheet.getName() !== TRACKER_DATA_SHEET) return;

  const ss = sheet.getParent();
  const dashboard = ss.getSheetByName(TRACKER_DASHBOARD_SHEET);
  const currentYear = dashboard ? dashboard.getRange('B1').getValue() : '';
  if (currentYear === '') return;

  const firstRow = Math.max(e.range.getRow(), 2);
  const lastRow = e.range.getLastRow();
  if (lastRow < 2) return;
  const numRows = lastRow - firstRow + 1;

  const yearRange = sheet.getRange(firstRow, 1, numRows, 1);
  const situationRange = sheet.getRange(firstRow, 4, numRows, 1);
  const years = yearRange.getValues();
  const situations = situationRange.getValues();

  let changed = false;
  for (let i = 0; i < numRows; i++) {
    if (years[i][0] === '' && situations[i][0] !== '') {
      years[i][0] = currentYear;
      changed = true;
    }
  }
  if (changed) yearRange.setValues(years);
}

function buildReactionTimeTracker() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  const dataSheet = getOrCreateSheet_(ss, TRACKER_DATA_SHEET);
  const dashSheet = getOrCreateSheet_(ss, TRACKER_DASHBOARD_SHEET);

  buildDataSheet_(dataSheet);
  buildDashboardSheet_(dashSheet);

  ss.setActiveSheet(dashSheet);
  ss.moveActiveSheet(1);
  ss.setActiveSheet(dataSheet);
  ss.moveActiveSheet(2);

  // Remove Sheets' default blank "Sheet1" if it is still sitting there empty.
  const def = ss.getSheetByName('Sheet1');
  if (def && ss.getSheets().length > 2 && def.getLastRow() === 0 && def.getLastColumn() === 0) {
    ss.deleteSheet(def);
  }

  ss.setActiveSheet(dashSheet);
  SpreadsheetApp.getUi().alert(
    'Tracker built.\n\n' +
    '1. Set Dashboard!B1 to the current school year.\n' +
    '2. Share this file (Share button, top right) — "Anyone at [your school ' +
    'domain] with the link" set to Editor — if you have not already.\n\n' +
    'Re-run this any time from SHULL Tools > Rebuild Tracker. It will not ' +
    'touch rows already entered.'
  );
}

function getOrCreateSheet_(ss, name) {
  let sheet = ss.getSheetByName(name);
  if (!sheet) sheet = ss.insertSheet(name);
  return sheet;
}

function buildDataSheet_(sheet) {
  const headers = [
    'School Year', 'Class Period', 'Student / Group', 'Situation (A/B/C)',
    'Drop 1 (cm)', 'Drop 2 (cm)', 'Drop 3 (cm)', 'Drop 4 (cm)',
    'Average (cm)', 'Reaction Time t (s)'
  ];
  sheet.getRange(1, 1, 1, headers.length).setValues([headers])
    .setFontWeight('bold').setBackground('#EDF0E5');
  sheet.setFrozenRows(1);

  // School Year: NOT a formula. It is snapshotted as a literal value by
  // onEdit_(), below, the first time a row gets a Situation entered — once
  // written it is never touched again, including when Dashboard!B1 changes
  // next year. A live formula here was tried and rejected: every row would
  // silently relabel itself to whatever B1 currently says, which means a
  // year change would retroactively rewrite every prior year's data and the
  // "This Year" filters would always be true for every row ever entered.
  // Caught in independent review before this ever ran — see change history.
  // Column I is Average, column J is Reaction Time; both remain formulas.
  const avgFormulas = [];
  const rtFormulas = [];
  for (let r = 2; r <= TRACKER_LAST_ROW; r++) {
    avgFormulas.push([`=IFERROR(AVERAGE(E${r}:H${r}),"")`]);
    rtFormulas.push([`=IFERROR(SQRT(2*(I${r}/100)/9.80),"")`]);
  }
  sheet.getRange(2, 9, TRACKER_LAST_ROW - 1, 1).setFormulas(avgFormulas);
  sheet.getRange(2, 10, TRACKER_LAST_ROW - 1, 1).setFormulas(rtFormulas);
  sheet.getRange(2, 9, TRACKER_LAST_ROW - 1, 2).setNumberFormat('0.00');

  // Situation dropdown — A, B, or C only.
  const situationRule = SpreadsheetApp.newDataValidation()
    .requireValueInList(['A', 'B', 'C'], true)
    .setAllowInvalid(false)
    .setHelpText('Enter A, B, or C — matching the situation you ran.')
    .build();
  sheet.getRange(2, 4, TRACKER_LAST_ROW - 1, 1).setDataValidation(situationRule);

  // Drop distances — 0 to 100 cm. A caught stick cannot exceed the meter
  // stick's own length, so this catches a cm/m slip or a stray extra digit
  // before it reaches the dashboard averages.
  const dropRule = SpreadsheetApp.newDataValidation()
    .requireNumberBetween(0, 100)
    .setAllowInvalid(false)
    .setHelpText('Enter the drop distance in cm, 0-100 (the meter stick is 100 cm).')
    .build();
  sheet.getRange(2, 5, TRACKER_LAST_ROW - 1, 4).setDataValidation(dropRule);

  sheet.setColumnWidth(1, 90);
  sheet.setColumnWidths(2, 2, 120);
  sheet.setColumnWidth(4, 110);
  sheet.setColumnWidths(5, 4, 80);
  sheet.setColumnWidths(9, 2, 100);

  protectHeaderRow_(sheet, headers.length);
}

function protectHeaderRow_(sheet, width) {
  sheet.getProtections(SpreadsheetApp.ProtectionType.RANGE).forEach(p => {
    if (p.getDescription() === 'Header row') p.remove();
  });
  const protection = sheet.getRange(1, 1, 1, width).protect()
    .setDescription('Header row')
    .setWarningOnly(false);
  protection.removeEditors(protection.getEditors());
  if (protection.canDomainEdit()) protection.setDomainEdit(false);
}

function buildDashboardSheet_(sheet) {
  // Read B1 BEFORE clearing the sheet — clear() wipes it first, which had
  // silently reset the current-year control cell to the hardcoded default
  // on every rebuild, contradicting "re-running never touches your data."
  const existingYear = sheet.getRange('B1').getValue();
  sheet.clear();
  sheet.getCharts().forEach(chart => sheet.removeChart(chart));

  sheet.getRange('A1').setValue('Current School Year').setFontWeight('bold');
  sheet.getRange('B1').setValue(existingYear || '2026-2027');
  sheet.getRange('A1:B1').setBackground('#FBDDA9');

  sheet.getRange('A3').setValue('This Year — Average Reaction Time').setFontWeight('bold');
  const labels = [
    ['Situation A (ordinary)'],
    ['Situation B (passenger warning)'],
    ['Situation C (counting backwards)']
  ];
  const filterFor = (situation) =>
    `=IFERROR(AVERAGE(FILTER(Data!$J$2:$J$${TRACKER_LAST_ROW},` +
    `Data!$D$2:$D$${TRACKER_LAST_ROW}="${situation}",` +
    `Data!$A$2:$A$${TRACKER_LAST_ROW}=$B$1)),"")`;
  const avgFormulas = [[filterFor('A')], [filterFor('B')], [filterFor('C')]];
  sheet.getRange(4, 1, 3, 1).setValues(labels);
  sheet.getRange(4, 2, 3, 1).setFormulas(avgFormulas);
  sheet.getRange(4, 2, 3, 1).setNumberFormat('0.000" s"');

  sheet.getRange('A8').setValue('Entries This Year').setFontWeight('bold');
  sheet.getRange('B8').setFormula(
    `=COUNTIFS(Data!$A$2:$A$${TRACKER_LAST_ROW},$B$1,Data!$D$2:$D$${TRACKER_LAST_ROW},"<>")`
  );

  // Both charts below get an EXPLICIT width/height rather than relying on
  // Apps Script's default (~600x371px). Left implicit, the two charts'
  // default footprints plausibly overlap each other. With explicit sizes,
  // the two charts are placed in disjoint ROW BANDS — rows 4-16 for the
  // this-year chart, rows 18+ for the header/pivot/trend-chart band — so
  // they cannot collide regardless of column position.
  const thisYearChart = sheet.newChart()
    .setChartType(Charts.ChartType.COLUMN)
    .addRange(sheet.getRange(4, 1, 3, 2))
    .setPosition(4, 4, 0, 0)
    .setOption('title', 'This Year: A vs B vs C')
    .setOption('legend', { position: 'none' })
    .setOption('series', { 0: { color: TRACKER_ACCENT } })
    .setOption('vAxis', { title: 'Reaction time (s)' })
    .setOption('width', 400)
    .setOption('height', 260)
    .build();
  sheet.insertChart(thisYearChart);

  sheet.getRange('A18').setValue('Year-Over-Year Average Reaction Time, by Situation')
    .setFontWeight('bold');
  sheet.getRange('A19').setFormula(
    `=IFERROR(QUERY(Data!A1:J${TRACKER_LAST_ROW},` +
    `"select A, avg(J) where A is not null and A <> '' group by A pivot D",1),` +
    `"No data yet — entries will appear once Data rows are filled in.")`
  );

  // Anchored to the RIGHT of the pivot table (column F, with column E left
  // as a gutter), not below it. The pivot table is fixed at 4 columns wide
  // (Year + A/B/C) but grows a row per year forever — anchoring below it
  // would eventually put the chart on top of its own data table after
  // enough years of use.
  const trendChart = sheet.newChart()
    .setChartType(Charts.ChartType.COLUMN)
    .addRange(sheet.getRange(19, 1, 60, 4))
    .setPosition(19, 6, 0, 0)
    .setOption('title', 'Class Average Reaction Time by Year')
    .setOption('vAxis', { title: 'Reaction time (s)' })
    .setOption('hAxis', { title: 'School year' })
    .setOption('colors', [TRACKER_ACCENT, TRACKER_ACCENT_B, '#2E3338'])
    .setOption('width', 520)
    .setOption('height', 320)
    .build();
  sheet.insertChart(trendChart);

  sheet.setColumnWidth(1, 220);
  sheet.setColumnWidth(2, 90);

  protectDashboardExceptControlCell_(sheet);
}

function protectDashboardExceptControlCell_(sheet) {
  sheet.getProtections(SpreadsheetApp.ProtectionType.SHEET).forEach(p => p.remove());
  const protection = sheet.protect().setDescription('Dashboard — aggregate view');
  protection.setUnprotectedRanges([sheet.getRange('B1')]);
  protection.removeEditors(protection.getEditors());
  if (protection.canDomainEdit()) protection.setDomainEdit(false);
}
