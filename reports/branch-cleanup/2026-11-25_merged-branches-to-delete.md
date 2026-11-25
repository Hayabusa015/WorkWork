# Merged branches to delete, 2026-11-25

**Status: NOT deleted.** The user approved the deletion in chat on 2026-11-25. The session's git proxy
answers 403 to a branch delete, so it has to be done from the user's own computer or the GitHub page.

Each branch below had 0 commits not in `main` when checked (`git rev-list --count origin/main..branch`).
`claude/sharp-bell-376uzt` was merged as PR #19 on 2026-11-25. All commits are already in `main`, so
deleting a branch loses no work. To restore one: `git push origin <sha>:refs/heads/<name>`.

**Keep:** `main`, `ccr-27d508d5-vgjdqt` (the working branch), and the three branches with unmerged work:
`claude/ecstatic-pascal-9cro1w`, `claude/funny-heisenberg-vu0q4r`, `design/armoury-workspace`.

## Delete them all (PowerShell or Git Bash, in a clone of the repo)

```
git push origin --delete ccr-009bc097-kut7zs ccr-0e393b80-9whfe8 ccr-3f548b83-n9ufnw ccr-409568ba-rajfce ccr-bdef5882-q3dzu3 ccr-d66537fd-2kw1gf ccr-eb4ada9c-82lvgm ccr-edc47f20-6cob4k claude/affectionate-cori-edhqsd claude/amazing-newton-knlwi2 claude/amazing-ritchie-hql8dw claude/app-redesign-dark-mode-r502l0 claude/blissful-dijkstra-xkbx5q claude/bold-edison-rclt4e claude/cool-bohr-qh1dfa claude/dazzling-maxwell-19rdw4 claude/eager-heisenberg-hk87nv claude/elegant-bohr-8hkbpj claude/elegant-bohr-8hkbpj-sept-archive claude/elegant-planck-f7l6hm claude/festive-noether-yhgdn7 claude/focused-mendel-cefeca claude/gracious-galileo-drxzqh claude/keen-cerf-my1dha claude/laughing-euler-dmaohs claude/lucid-maxwell-d8ddes claude/next-build-phase-2vuvzm claude/nice-fermat-vehaxv claude/physics-unit-1-study-guide-c1wzx2 claude/physics-unit-2-slides-g0q9a9 claude/reaction-time-free-fall-lab-jfktxs claude/repo-refamiliarization-zykuqi claude/upbeat-hawking-p2d08y claude/visual-design-student-learning-dhkzof claude/wizardly-mendel-p73co4 claude/wonderful-galileo-b4f6mb claude/zealous-lovelace-nyknbz claude/zealous-lovelace-rngqm4 claude/zealous-lovelace-vhmwmt feature/repository-desk claude/sharp-bell-376uzt
```

| Branch | Last commit | Date |
|---|---|---|
| ccr-009bc097-kut7zs | 1724a39956419f60930c21d03654aa738c8fa431 | 2026-11-04 |
| ccr-0e393b80-9whfe8 | 9b1c8a7faca5f350c0bee0182ae2d561cbe5f76b | 2026-10-16 |
| ccr-3f548b83-n9ufnw | 0c766a2a24acd08cdd83cbc4cf1079f2b45b5407 | 2026-10-19 |
| ccr-409568ba-rajfce | b99bec312290a3fa44b96e16bd3483d7f9831f57 | 2026-11-16 |
| ccr-bdef5882-q3dzu3 | 1b584e890a0204b8b0ad1ffbf4ea2b2aad2f7a4a | 2026-11-13 |
| ccr-d66537fd-2kw1gf | 8d94e7b703ccdb51c4fe1ab19cbd4fac93eab1a3 | 2026-10-04 |
| ccr-eb4ada9c-82lvgm | c57bb6e41f5b848d77b4d1766bf80df299795328 | 2026-11-10 |
| ccr-edc47f20-6cob4k | 706a80e92fa689db2309fedc2893991059d138d5 | 2026-10-28 |
| claude/affectionate-cori-edhqsd | 5850742b994334f02652bb895856e7b40726dd2f | 2026-11-04 |
| claude/amazing-newton-knlwi2 | 429965da78e1f64dbb79c9457fc280fdad02b082 | 2026-10-23 |
| claude/amazing-ritchie-hql8dw | a38678a349afe638cbdf69bb0a6dc78c4122b32a | 2026-11-24 |
| claude/app-redesign-dark-mode-r502l0 | 6126930b6148cf6fc3e83090273a900eff2c3870 | 2026-09-21 |
| claude/blissful-dijkstra-xkbx5q | 4958169d1fa20b31ed88f82b93a427870cc50a46 | 2026-11-09 |
| claude/bold-edison-rclt4e | 8fde8136d02642c18fa5cca6a0fa89ec95cb6531 | 2026-10-30 |
| claude/cool-bohr-qh1dfa | 1721868a6f18d7325540755905068de9df677586 | 2026-10-28 |
| claude/dazzling-maxwell-19rdw4 | 16f2794b1897a3bb3ed6fb2e50e5e719f71ad98f | 2026-09-24 |
| claude/eager-heisenberg-hk87nv | 2830fa61bbcdbc1e8d512f55085c9232ce1ddcbf | 2026-11-10 |
| claude/elegant-bohr-8hkbpj | 3665fa08a4ffd49b5ec00803dbc6bc44fdc2c76f | 2026-11-11 |
| claude/elegant-bohr-8hkbpj-sept-archive | f003fb077e59752e7e3941ae0498bc1ef1f6278c | 2026-09-25 |
| claude/elegant-planck-f7l6hm | 182d1b7be521a78a500d719aaeab775fe1e512fa | 2026-11-23 |
| claude/festive-noether-yhgdn7 | 1f2069989510480041e8821860d0c9523994b238 | 2026-10-22 |
| claude/focused-mendel-cefeca | 85d0d9e80dd26566463dc90ee40be77b2508ef93 | 2026-11-20 |
| claude/gracious-galileo-drxzqh | 9793fb8f1caff4d87b84af1c78901b782f74e524 | 2026-10-15 |
| claude/keen-cerf-my1dha | 839eb810eefc89e793db6405c1162f84dda84185 | 2026-11-12 |
| claude/laughing-euler-dmaohs | 84d07737c144f80a0707ad223b9919eb6830e069 | 2026-10-06 |
| claude/lucid-maxwell-d8ddes | 6d7e21b6c56609bc173be8d1b37c0a03e67598f5 | 2026-11-06 |
| claude/next-build-phase-2vuvzm | 1b2617935292608794eeaeefa274f9f01a239bb4 | 2026-09-18 |
| claude/nice-fermat-vehaxv | bdfacd773e73ae4cd49dee347eb2ff8422cd0917 | 2026-10-15 |
| claude/physics-unit-1-study-guide-c1wzx2 | 853eb718ef5f59461e43a076ff616decb47af221 | 2026-09-25 |
| claude/physics-unit-2-slides-g0q9a9 | 481dd344132c14b7b1a8c434ae67160416c91866 | 2026-10-07 |
| claude/reaction-time-free-fall-lab-jfktxs | ea97e02c13a03231724db53544e860e3fb997785 | 2026-09-24 |
| claude/repo-refamiliarization-zykuqi | 3dd1c72ade08485caaccdbe03ffdd6c2e8d01ad7 | 2026-09-14 |
| claude/upbeat-hawking-p2d08y | a7217f4a0216140984abbc2c076014e25c5e3840 | 2026-09-28 |
| claude/visual-design-student-learning-dhkzof | c2cff9116babbabfa6518ec70f5bad4b3fe0f17a | 2026-09-16 |
| claude/wizardly-mendel-p73co4 | 1dcf5f02a41ef55e10abbf4e45f329115ef0b000 | 2026-10-29 |
| claude/wonderful-galileo-b4f6mb | 62aa38ee77a31306494d86560f6cfae38b566853 | 2026-09-17 |
| claude/zealous-lovelace-nyknbz | e5d92753976463c1feb294041a8e66468680507b | 2026-11-15 |
| claude/zealous-lovelace-rngqm4 | c5829200564bd013427d7e2dbde952b7e684e0b8 | 2026-11-08 |
| claude/zealous-lovelace-vhmwmt | b955feb7e8bba23ca0aef8ce0f20ba7212fb44d2 | 2026-11-22 |
| feature/repository-desk | 523084d9c2161d8a4345dd1c584aefe169b2997e | 2026-11-23 |
| claude/sharp-bell-376uzt | d6869b3c983a33182d272dc1e371c6cab2e19ba4 | 2026-11-23 |
