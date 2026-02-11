# Claude Code Instructions

## Architecture
- Single `index.html` file — all HTML, CSS, and JS inline
- No build tools, no frameworks, no dependencies (except Prism.js via CDN)
- Fonts: Sora (sans) and DM Mono (monospace) from Google Fonts

## Deployment
- Hosted on **Vercel** (static) — auto-deploys from GitHub
- PRs get **preview deployments** with Vercel bot comments
- Merges to `main` trigger **production deployment** to agentic-coding-fitness.vercel.app
- No manual `vercel --prod` needed

## Development Workflow
1. `git checkout -b feature-name`
2. Edit `index.html`
3. Test: open in browser + check at 375px mobile width + check DevTools console
4. `git commit` → `git push -u origin feature-name`
5. `gh pr create` (uses `.github/pull_request_template.md`)
6. Wait for Vercel preview deployment check
7. Squash merge to `main`

## PR Conventions
- One logical change per PR
- Use the PR template in `.github/pull_request_template.md`
- Test at 375px width for mobile
- No console errors

## Design System
- Theme: "Cybertruck x Optimus x Ferrari x Tron" — angular, sharp, zero border-radius
- Background: #050507 (near-black)
- Primary accent: Ferrari red #ff2800
- Secondary accent: Tron cyan #00e0ff
- Phase colors: Blue (#4a7dff), Green (#00c853), Orange (#ff6d00), Purple (#aa00ff)
- All corners sharp (border-radius: 0px)
- Code blocks: dark theme with Prism.js syntax highlighting

## Content Structure
- 16-week curriculum, 4 phases
- Each week: warmup → theory → demo → break → hands-on → test → sharing
- Code examples in Python
- Quiz questions with reveal/hide answers
