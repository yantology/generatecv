# GitHub Actions Troubleshooting Guide

This document provides solutions for common GitHub Actions issues in the generatecv project.

## Recent Fixes Applied

### 1. Permission Errors (403 Forbidden)

**Problem**: GitHub Actions workflows failing with "Resource not accessible by integration" and permission errors.

**Solutions Applied**:

#### Security Workflow (`security.yml`)
- Added proper `permissions` block:
  ```yaml
  permissions:
    contents: write
    issues: write
    pull-requests: write
    actions: read
    security-events: write
  ```
- Added explicit `github-token` parameter to `github-script` actions
- Improved error handling with try-catch blocks
- Made repository operations conditional and fault-tolerant

#### Documentation Workflow (`docs.yml`)
- Added `permissions` block for GitHub Pages:
  ```yaml
  permissions:
    contents: write
    pages: write
    id-token: write
  ```

### 2. Safety Tool Deprecation

**Problem**: The `safety check` command is deprecated and causing errors.

**Solution**: 
- Replaced `safety` with `pip-audit` as the primary vulnerability scanner
- Added `safety` as a backup option
- Implemented graceful fallback when tools fail
- Updated dependency counting to use `importlib.metadata` instead of deprecated `pkg_resources`

### 3. MkDocs Build Failures

**Problem**: Documentation build failing due to navigation configuration issues.

**Solutions**:
- Fixed navigation links in `mkdocs.yml` (changed `api/` to `api/index.md`)
- Removed `--strict` mode and used `--verbose` for better debugging
- Created complete documentation structure with all required files
- Ensured consistent cross-references between documentation files

### 4. Git Push Permission Issues

**Problem**: GitHub Actions unable to push commits back to repository.

**Solutions**:
- Added proper git configuration with `github-actions[bot]` user
- Made git operations fault-tolerant with `|| echo` fallbacks
- Added checkout with explicit token parameter
- Made security report saving conditional on main branch only

## Common Issues and Solutions

### Permission Denied Errors

**Symptoms**:
- `403 Client Error`
- `Permission to repository denied`
- `Resource not accessible by integration`

**Solutions**:
1. Add proper `permissions` block to workflow
2. Use `github-token: ${{ secrets.GITHUB_TOKEN }}` in actions
3. Check repository settings for Actions permissions
4. Ensure token has required scopes

### Security Scanning Failures

**Symptoms**:
- `safety` command deprecated warnings
- Network errors during vulnerability scanning
- Empty or missing scan results

**Solutions**:
1. Use multiple scanning tools with fallbacks
2. Handle network timeouts gracefully
3. Parse tool output correctly
4. Set appropriate output variables

### Documentation Build Issues

**Symptoms**:
- MkDocs navigation warnings
- Missing documentation files
- Strict mode failures

**Solutions**:
1. Create all referenced documentation files
2. Fix navigation configuration
3. Use relative links consistently
4. Test builds locally before pushing

### Git Operations Failing

**Symptoms**:
- `fatal: unable to access repository`
- Authentication failures during push
- Empty commits causing errors

**Solutions**:
1. Configure git user properly
2. Use fault-tolerant commands with fallbacks
3. Check for changes before committing
4. Handle authentication with proper tokens

## Prevention Strategies

### 1. Local Testing

Always test workflows locally using tools like:
- `act` for running GitHub Actions locally
- `mkdocs serve` for documentation
- `pip-audit` and security tools manually

### 2. Incremental Changes

- Make small, focused changes to workflows
- Test each component separately
- Use workflow debugging with verbose logging

### 3. Proper Error Handling

- Use `|| echo` for non-critical operations
- Implement try-catch blocks in scripts
- Set appropriate exit codes
- Log meaningful error messages

### 4. Permissions Management

- Use least-privilege principle
- Explicitly declare required permissions
- Test with different token scopes
- Monitor GitHub Actions logs for permission issues

## Debugging Tips

### Enable Debug Logging

Add to workflow:
```yaml
env:
  ACTIONS_STEP_DEBUG: true
  ACTIONS_RUNNER_DEBUG: true
```

### Check Workflow Logs

1. Go to Actions tab in GitHub repository
2. Click on failed workflow run
3. Expand failed steps to see detailed logs
4. Look for specific error messages and stack traces

### Test Components Individually

```bash
# Test documentation build
uv run mkdocs build --verbose

# Test security scanning
uv run pip-audit --format=columns

# Test code scanning
uv run bandit -r src/
```

### Validate Workflow Syntax

Use GitHub CLI or online validators:
```bash
gh workflow view security.yml
```

## Emergency Procedures

### Disable Failing Workflows

If workflows are causing critical issues:

1. **Temporarily disable**:
   - Go to Actions tab → Select workflow → Disable workflow

2. **Emergency fix**:
   - Create hotfix branch
   - Fix workflow files
   - Test locally
   - Create emergency PR

3. **Rollback**:
   - Revert problematic commits
   - Restore previous working versions

### Contact Points

- GitHub Actions Documentation: https://docs.github.com/en/actions
- Community Support: GitHub Community Forums
- Emergency: Repository maintainers

## Monitoring and Maintenance

### Regular Checks

- Monitor workflow success rates
- Update deprecated actions and tools
- Review security scan results
- Keep dependencies updated

### Scheduled Maintenance

- Monthly review of workflow performance
- Quarterly update of action versions
- Annual security and compliance review

---

**Last Updated**: 2025-05-25  
**Version**: 1.0  
**Maintainer**: GitHub Actions Team