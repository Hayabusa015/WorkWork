# ARCHIVED — Geology earth palette

**Status:** DEPRECATED · **Superseded:** 2026-09-07 by SHULL-CHG-0003 (Terra Teal + Rust Orange)
**Was authoritative in:** `_Brand/Standards/SHULL_System_Governance.md` §8, which records it as
**confirmed** and already in use

Canyon Umber · Basalt Brown · Rust Red · Amber Ochre · Sage Moss · Sandstone

*Exact hex values were never recorded in any file available to this migration — the palette was
named in governance §8 and applied in a built packet, but its token table was not written down.
That is itself the defect this archive exists to prevent.*

## What it was for

A print-first earth-tone system for a visual, hands-on course whose handouts are photocopied more
than any other. It solved a different problem than a projection accent pair does, which is why both
existed.

## Why it was superseded

Spec Part 30 replaces per-course palette *exceptions* with one shared system carrying per-course
identity. Under that model Geology has no separate print palette; it has Terra Teal and Rust Orange
across all media.

## Materials built on it — leave as-is

**The built Geology U1 packet.** It is now off-palette. Under the no-retrofit policy it stays as
built. **Do not flag it as a brand defect.**

## One thing the replacement must watch

Terra Teal and Rust Orange sit six grey levels apart and are effectively identical photocopied. The
earth palette did not have that problem. Every Geology categorical use of both **must** differ by
border and label as well as fill. `scripts/measure_tokens.py` reports it on every run.
