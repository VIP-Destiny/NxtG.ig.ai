# NextGigAI GitHub Setup Guide

## 1. Main Platform Repository Setup

### Create Main Repository
1. Go to [GitHub](https://github.com)
2. Click '+ New repository'
3. Settings:
   - Owner: `NxtG.ai`
   - Repository name: `NxtG.ig.ai`
   - Description: `AI-powered career acceleration platform`
   - Public repository
   - Add README.md
   - Add .gitignore (Python)
   - Add MIT License

### Clone and Setup
```bash
# Clone the repository
git clone https://github.com/NxtG.ai/NxtG.ig.ai.git
cd NxtG.ig.ai

# Create develop branch
git checkout -b develop
git push -u origin develop
```

### Configure Repository Settings
1. Go to repository Settings
2. Branches:
   - Add branch protection rules for `main` and `develop`
   - Require pull request reviews
   - Require status checks
   - Include administrators
3. Collaborators:
   - Add team members
4. Actions:
   - Enable GitHub Actions

## 2. Resume Formatter Module Setup

### Create Module Repository
1. Go to [GitHub](https://github.com)
2. Click '+ New repository'
3. Settings:
   - Owner: `NxtG.ai`
   - Repository name: `nextgig-resume-formatter`
   - Description: `AI-powered resume formatting module for NextGigAI platform`
   - Public repository
   - Don't initialize with files

### Setup Module Repository
```bash
# Create a new directory for the module
mkdir nextgig-resume-formatter
cd nextgig-resume-formatter

# Initialize git
git init
git checkout -b main

# Copy module files
cp -r /path/to/NextGigAI/Modules/res_formatter/* .

# Add and commit files
git add .
git commit -m "🚀 Initial commit: Resume Formatter Module"

# Add remote and push
git remote add origin https://github.com/NxtG.ai/nextgig-resume-formatter.git
git push -u origin main

# Create and push develop branch
git checkout -b develop
git push -u origin develop
```

### Configure Module Repository Settings
1. Go to repository Settings
2. Branches:
   - Add branch protection rules
   - Require pull request reviews
   - Require status checks
3. Secrets:
   - Add `PYPI_API_TOKEN` for package publishing

## 3. Set Up Git Submodules

### In Main Repository
```bash
# Add Resume Formatter as submodule
cd NextGigAI
git submodule add https://github.com/NxtG.ai/nextgig-resume-formatter.git Modules/res_formatter
git commit -m "📦 Add Resume Formatter module as submodule"
git push
```

## 4. Development Workflow

### Branching Strategy
- `main` - Default branch, represents production-ready state
  - Only accepts merges from `develop` via PR
  - Each merge creates a new release
  - Protected branch with required reviews
  
- `develop` - Integration branch
  - Contains completed features for next release
  - Protected branch with required reviews
  - Features are merged here first
  
- `feature/*` - Feature branches
  - Created from: `develop`
  - Merge into: `develop`
  - Naming: `feature/description-of-feature`
  
- `hotfix/*` - Hotfix branches
  - Created from: `main`
  - Merge into: `main` and `develop`
  - For urgent production fixes
  
- `release/*` - Release branches
  - Created from: `develop`
  - Merge into: `main` and `develop`
  - For release preparation

### Branch Protection
- `main` and `develop` are protected
- Require pull request reviews
- Require CI checks to pass
- No direct pushes allowed

### Main Platform
```bash
# Create feature branch
git checkout develop
git pull origin develop
git checkout -b feature/new-feature

# Make changes
# ... work on your feature ...

# Commit and push
git add .
git commit -m "✨ Add new feature"
git push origin feature/new-feature

# Create Pull Request to develop
# After review and merge to develop:
git checkout develop
git pull origin develop
```

### Module Development
```bash
# In module directory
cd Modules/res_formatter

# Create feature branch
git checkout develop
git pull origin develop
git checkout -b feature/new-template

# Make changes
# ... work on your template ...

# Run tests
pytest

# Commit and push
git add .
git commit -m "🎨 Add new resume template"
git push origin feature/new-template

# Create Pull Request to develop
```

## 5. Release Process

### Module Release
1. Update version in `pyproject.toml`
2. Update `CHANGELOG.md`
3. Create PR from `develop` to `main`
4. After merge, tag the release:
```bash
git checkout main
git pull origin main
git tag -a v0.1.0 -m "Release v0.1.0"
git push origin v0.1.0
```

### Platform Release
1. Update submodules to latest versions
2. Update platform version
3. Create PR from `develop` to `main`
4. Tag release after merge

## 6. Common Tasks

### Update Submodule
```bash
# In main repository
git submodule update --remote Modules/res_formatter
git add Modules/res_formatter
git commit -m "⬆️ Update Resume Formatter module"
git push
```

### Run CI/CD Locally
```bash
# Install pre-commit hooks
pre-commit install

# Run tests
pytest

# Build package
python -m build

# Check package
twine check dist/*
```

## 7. Troubleshooting

### Submodule Issues
```bash
# Reset submodule
git submodule deinit -f Modules/res_formatter
git submodule update --init --recursive

# Update all submodules
git submodule update --remote --merge
```

### Branch Issues
```bash
# Reset to remote
git fetch origin
git reset --hard origin/develop

# Clean untracked files
git clean -fd
```

## 8. Best Practices

1. **Commit Messages**
   - Use emoji prefixes
   - Be descriptive but concise
   - Reference issues

2. **Branching**
   - Keep branches focused
   - Delete after merging
   - Regular rebasing

3. **Code Quality**
   - Run linters before commit
   - Write tests
   - Update documentation

4. **Reviews**
   - Detailed descriptions
   - Screenshots if UI changes
   - Test instructions

## Need Help?

- Check [GitHub Docs](https://docs.github.com)
- Open an issue
- Ask in discussions
