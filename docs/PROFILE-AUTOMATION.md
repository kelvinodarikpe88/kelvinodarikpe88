# Profile graphics and automation

The profile keeps the original detailed domain format. Its main navigation is Hiring brief · CISO brief · Project index.

## What runs automatically

GitHub Actions runs `python scripts/check_profile.py` on main pushes, pull requests and manual dispatch. It checks local document links, raw profile-image targets, valid SVG XML, prohibited SVG embedded content, byte-identical generated diagrams, the requested navigation, a reduced-motion still and finite GIF looping.

The workflow has read-only repository permissions. It never rewrites claims, fabricates metrics, emails recruiters, modifies projects, or requests new account access. It does not claim to test every external website or search-engine ranking.

## Rebuild the original diagrams

`python build_profile_assets.py` generates the eight original SVGs. Optional CairoSVG produces their PNG previews. Outcome edits belong in the README, metrics ledger and generator together; preserve provenance labels and documented gaps.

## Rebuild the motion graphic

Install Pillow in a local environment and use the official librsvg `rsvg-convert` binary. Then run `python scripts/build_motion.py`. This generates a 36-frame GIF and static PNG/SVG from `scripts/motion_svg.py`.

The animation illustrates signal → detection → AI context → human review → bounded action → evidence. It uses synthetic workflow labels, makes no network or model calls, and is not live platform telemetry. It plays three cycles, then stops. A `picture` source displays the static PNG for reduced-motion preferences; the still is also linked directly.

GitHub profile READMEs cannot host a JavaScript application or a live autonomous AI agent. Interactive product workflows remain on the public Veriseya preview, with deployment limits stated in the profile.
