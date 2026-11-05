/* Drawing primitives and the molecules for Units 4-5: one copy, used by the slide deck
 * (build.js) and by the guided-notes key drawings (key_structures.js). A molecule drawn
 * twice is a molecule that can disagree with itself.
 *
 *   const M = require("./molecules")(pres);   // pres: a pptxgenjs presentation
 */
const K = require("../../tokens.generated");

module.exports = function (pres) {
const G = K.ground, CO = K.courses.chemistry, F = K.fonts;
const INK = G.asphalt, PAPER = G.parchment, DEEP = CO.primaryDeep, ORANGE = CO.primary, CYAN = CO.secondary;
/* ---------------------------------------------------------------- primitives */
/* Archivo has no superscript plus/minus glyphs, so charges are written as superscript runs. */
function rich(text, base = {}) {
  const lines = String(text).split("\n"), runs = [];
  lines.forEach((ln, li) => {
    const parts = ln.split(/([⁺⁻])/).filter((p) => p !== "");
    if (!parts.length) parts.push("");
    parts.forEach((p, pi) => {
      const sup = p === "⁺" || p === "⁻";
      const o = Object.assign({}, base, sup ? { superscript: true } : {});
      if (pi === parts.length - 1 && li < lines.length - 1) o.breakLine = true;
      runs.push({ text: sup ? (p === "⁺" ? "+" : "−") : p, options: o });
    });
  });
  return runs;
}
let seq = 0;
const nm = (click) => `c${click || 0}_${++seq}`;

function line(s, x1, y1, x2, y2, o = {}) {
  s.addShape(pres.shapes.LINE, {
    x: Math.min(x1, x2), y: Math.min(y1, y2),
    w: Math.max(Math.abs(x2 - x1), 0.001), h: Math.max(Math.abs(y2 - y1), 0.001),
    flipH: x2 < x1, flipV: y2 < y1,
    line: { color: o.color || INK, width: o.width || 2.5, dashType: o.dash || "solid",
            endArrowType: o.end, beginArrowType: o.begin },
    objectName: nm(o.click),
  });
}
function dot(s, x, y, d, color, click) {
  s.addShape(pres.shapes.OVAL, { x: x - d / 2, y: y - d / 2, w: d, h: d,
    fill: { color }, line: { color, width: 0.5 }, objectName: nm(click) });
}
function oval(s, x, y, w, h, o = {}) {
  s.addShape(pres.shapes.OVAL, { x: x - w / 2, y: y - h / 2, w, h, rotate: o.rotate || 0,
    fill: o.fill ? { color: o.fill, transparency: o.transparency || 0 } : { type: "none" },
    line: o.line ? { color: o.line, width: o.lineWidth || 1.5, dashType: o.dash || "solid" } : { type: "none" },
    objectName: nm(o.click) });
}
function rect(s, x, y, w, h, color) {
  s.addShape(pres.shapes.RECTANGLE, { x, y, w, h, fill: { color }, line: { color, width: 0.5 }, objectName: nm(0) });
}
function label(s, text, cx, cy, w, h, o = {}) {
  s.addText(rich(text), { x: cx - w / 2, y: cy - h / 2, w, h, fontFace: o.face || F.body, fontSize: o.size || 16,
    bold: o.bold !== false, color: o.color || INK, align: o.align || "center", valign: "middle", margin: 0,
    objectName: nm(o.click) });
}
/* A dipole arrow: points at the delta-minus end, cross near the delta-plus tail. */
function dipole(s, x1, y1, x2, y2, color, click, width = 2.5) {
  line(s, x1, y1, x2, y2, { color, width, end: "triangle", click });
  const L = Math.hypot(x2 - x1, y2 - y1), ux = (x2 - x1) / L, uy = (y2 - y1) / L;
  const cx = x1 + ux * 0.13, cy = y1 + uy * 0.13, h = 0.09;
  line(s, cx - uy * h, cy + ux * h, cx + uy * h, cy - ux * h, { color, width, click });
}

/* ------------------------------------------------------------ Lewis structures
 * mol = { atoms: {id: [sym, x, y]}, bonds: [[a, b, order]], pairs: [[atom, angleDeg]] }
 * Coordinates are in bond lengths; u converts to inches. Angles are screen angles
 * (0 = right, 90 = down). clicks = { atoms, bonds, pairs } choose the reveal step of each
 * layer; a bond or pair can override with a 4th element. */
function lewis(s, mol, cx, cy, u, o = {}) {
  const fs_ = o.fs || 32, k = fs_ / 32, fg = o.color || INK, ck = o.clicks || {};
  const P = (id) => [cx + mol.atoms[id][1] * u, cy + mol.atoms[id][2] * u];
  const wide = (id) => mol.atoms[id][0].length > 1;
  const reach = (id, ang, base) => {      // ellipse around the glyph: wider for two letters
    const rx = base * k * (wide(id) ? 1.45 : 1), ry = base * k, a = ang * Math.PI / 180;
    return Math.hypot(rx * Math.cos(a), ry * Math.sin(a)) * 1.0;
  };
  for (const [a, b, order, c, col] of mol.bonds) {
    const [x1, y1] = P(a), [x2, y2] = P(b);
    const ang = Math.atan2(y2 - y1, x2 - x1) * 180 / Math.PI;
    const t1 = reach(a, ang, 0.24), t2 = reach(b, ang + 180, 0.24);
    const L = Math.hypot(x2 - x1, y2 - y1), ux = (x2 - x1) / L, uy = (y2 - y1) / L;
    const sx = x1 + ux * t1, sy = y1 + uy * t1, ex = x2 - ux * t2, ey = y2 - uy * t2;
    if (order === "wedge" || order === "dash") {   // 3D bond, narrow at a, wide at b
      const half = 0.085 * k, click = c !== undefined ? c : ck.bonds;
      if (order === "wedge") {
        const pts = [[sx, sy], [ex - uy * half, ey + ux * half], [ex + uy * half, ey - ux * half]];
        const minx = Math.min(...pts.map((q) => q[0])), miny = Math.min(...pts.map((q) => q[1]));
        const w = Math.max(...pts.map((q) => q[0])) - minx, h = Math.max(...pts.map((q) => q[1])) - miny;
        s.addShape(pres.shapes.CUSTOM_GEOMETRY, { x: minx, y: miny, w: Math.max(w, 0.01), h: Math.max(h, 0.01),
          points: [...pts.map((q) => ({ x: q[0] - minx, y: q[1] - miny })), { close: true }],
          fill: { color: fg }, line: { color: fg, width: 0.5 }, objectName: nm(click) });
      } else {
        const n = 6;
        for (let i = 0; i < n; i++) {
          const f = (i + 0.5) / n, hx = half * (0.25 + 0.75 * f);
          const mx = sx + (ex - sx) * f, my = sy + (ey - sy) * f;
          line(s, mx - uy * hx, my + ux * hx, mx + uy * hx, my - ux * hx, { color: fg, width: 1.5, click });
        }
      }
      continue;
    }
    const offs = order === 1 ? [0] : order === 2 ? [-0.065 * k, 0.065 * k] : [-0.1 * k, 0, 0.1 * k];
    offs.forEach((d, i) => line(s, x1 + ux * t1 - uy * d, y1 + uy * t1 + ux * d, x2 - ux * t2 - uy * d, y2 - uy * t2 + ux * d,
      { color: (col && i === offs.length - 1) ? col : fg, width: 2.75 * Math.max(k, 0.7),
        click: c !== undefined ? c : ck.bonds }));
  }
  for (const [id, ang, c, n] of mol.pairs) {     // n = 1 draws a single (unpaired) electron
    const [x, y] = P(id), a = ang * Math.PI / 180, r = reach(id, ang, 0.33);
    const px = x + Math.cos(a) * r, py = y + Math.sin(a) * r, sp = 0.068 * k;
    for (const sgn of (n === 1 ? [0] : [-1, 1])) dot(s, px - Math.sin(a) * sp * sgn, py + Math.cos(a) * sp * sgn, 0.085 * k, fg,
      c !== undefined ? c : ck.pairs);
  }
  for (const [id, [sym]] of Object.entries(mol.atoms)) {
    const [x, y] = P(id);
    label(s, sym, x, y, 0.42 * k * (sym.length > 1 ? 1.7 : 1), 0.5 * k,
      { size: fs_, face: F.display, color: fg, click: ck.atoms });
  }
  return P;
}
const at = (deg, r = 1) => [Math.cos(deg * Math.PI / 180) * r, Math.sin(deg * Math.PI / 180) * r];

/* The molecules. Each is drawn exactly as a student would on paper. */
const MOL = {
  BF3: { atoms: { B: ["B", 0, 0], F1: ["F", ...at(-90)], F2: ["F", ...at(150)], F3: ["F", ...at(30)] },
         bonds: [["B", "F1", 1], ["B", "F2", 1], ["B", "F3", 1]],
         pairs: [["F1", -90], ["F1", 0], ["F1", 180], ["F2", 150], ["F2", 60], ["F2", 240], ["F3", 30], ["F3", 120], ["F3", -60]] },
  CO2_single: { atoms: { O1: ["O", -1, 0], C: ["C", 0, 0], O2: ["O", 1, 0] },
         bonds: [["O1", "C", 1], ["C", "O2", 1]],
         pairs: [["O1", 180], ["O1", -90], ["O1", 90], ["O2", 0], ["O2", -90], ["O2", 90]] },
  CO2: { atoms: { O1: ["O", -1, 0], C: ["C", 0, 0], O2: ["O", 1, 0] },
         bonds: [["O1", "C", 2], ["C", "O2", 2]],
         pairs: [["O1", 135], ["O1", 225], ["O2", 45], ["O2", -45]] },
  CH2O_single: { atoms: { C: ["C", 0, 0], O: ["O", ...at(-90)], H1: ["H", ...at(150)], H2: ["H", ...at(30)] },
         bonds: [["C", "O", 1], ["C", "H1", 1], ["C", "H2", 1]],
         pairs: [["O", -90], ["O", 0], ["O", 180]] },
  CH2O: { atoms: { C: ["C", 0, 0], O: ["O", ...at(-90)], H1: ["H", ...at(150)], H2: ["H", ...at(30)] },
         bonds: [["C", "O", 2], ["C", "H1", 1], ["C", "H2", 1]],
         pairs: [["O", -135], ["O", -45]] },
  H2O: { atoms: { O: ["O", 0, 0], H1: ["H", ...at(142.25)], H2: ["H", ...at(37.75)] },
         bonds: [["O", "H1", 1], ["O", "H2", 1]], pairs: [["O", -135], ["O", -45]] },
  NH3: { atoms: { N: ["N", 0, 0], H1: ["H", ...at(155)], H2: ["H", ...at(90)], H3: ["H", ...at(25)] },
         bonds: [["N", "H1", 1], ["N", "H2", 1], ["N", "H3", 1]], pairs: [["N", -90]] },
  CCl4: { atoms: { C: ["C", 0, 0], A: ["Cl", 0, -1], B: ["Cl", 1, 0], D: ["Cl", 0, 1], E: ["Cl", -1, 0] },
         bonds: [["C", "A", 1], ["C", "B", 1], ["C", "D", 1], ["C", "E", 1]],
         pairs: [["A", -90], ["A", 0], ["A", 180], ["B", 0], ["B", -90], ["B", 90],
                 ["D", 90], ["D", 0], ["D", 180], ["E", 180], ["E", -90], ["E", 90]] },
  HCl: { atoms: { H: ["H", -0.5, 0], Cl: ["Cl", 0.5, 0] }, bonds: [["H", "Cl", 1]],
         pairs: [["Cl", 0], ["Cl", -90], ["Cl", 90]] },
};

/* Bond dipole drawn beside a bond, from the delta-plus atom toward the delta-minus atom. */
function bondDipole(s, P, from, to, side, color, click, off = 0.2, f0 = 0.22, f1 = 0.78) {
  const [x1, y1] = P(from), [x2, y2] = P(to);
  const L = Math.hypot(x2 - x1, y2 - y1), ux = (x2 - x1) / L, uy = (y2 - y1) / L;
  const nx = -uy * side, ny = ux * side;
  dipole(s, x1 + ux * L * f0 + nx * off, y1 + uy * L * f0 + ny * off,
            x1 + ux * L * f1 + nx * off, y1 + uy * L * f1 + ny * off, color, click);
}


return { rich, line, dot, oval, rect, label, dipole, lewis, at, MOL, bondDipole,
         INK, PAPER, DEEP, ORANGE, CYAN };
};
