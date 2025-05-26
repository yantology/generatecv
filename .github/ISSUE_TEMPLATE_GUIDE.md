# Issue Template System Guide

## Overview

This repository uses a comprehensive issue template system to ensure consistent, high-quality issue reporting and efficient triage. All issues must use one of the provided templates.

## Available Templates

### 🐛 Bug Report (`bug_report.yml`)
**Use when:** Reporting software bugs, errors, or unexpected behavior
- **Required fields:** Problem description, reproduction steps, expected vs actual behavior
- **Auto-labels:** `bug`, `needs-triage`
- **Priority detection:** Automatically detects critical, high, medium, or low priority
- **Platform detection:** Auto-labels based on OS (Windows, macOS, Linux)

### ✨ Feature Request (`feature_request.yml`)
**Use when:** Suggesting new features or enhancements
- **Required fields:** Problem description, proposed solution, use cases
- **Auto-labels:** `enhancement`, `needs-triage`
- **Complexity estimation:** Simple, medium, complex, or very complex
- **Priority assessment:** Based on business impact and user needs

### 📚 Documentation (`documentation.yml`)
**Use when:** Reporting documentation issues or improvements
- **Required fields:** Location, issue description, suggested improvement
- **Auto-labels:** `documentation`, `needs-triage`
- **Types:** Missing docs, incorrect info, unclear explanations, typos

### ❓ Question/Help (`question.yml`)
**Use when:** Asking questions or seeking help
- **Required fields:** Question, context, what you've tried
- **Auto-labels:** `question`, `help-wanted`
- **Categories:** Usage help, configuration, troubleshooting, best practices

## Automated Features

### 🏷️ Auto-Labeling System
Issues are automatically labeled based on:
- **Content analysis:** Keywords in title and description
- **Template type:** Bug, feature, docs, question
- **Priority level:** Critical, high, medium, low
- **Technology stack:** Python, JavaScript, Docker, etc.
- **Platform/OS:** Windows, macOS, Linux, web, mobile
- **Effort estimation:** Small, medium, large, extra-large
- **Component affected:** API, UI, database, tests

### 🚨 Priority Detection
- **Critical:** Security issues, data loss, production failures
- **High:** Breaking changes, major functionality impact
- **Medium:** Standard bugs and features
- **Low:** Minor improvements, cosmetic issues

### 📋 Template Validation
- **Compliance scoring:** Issues receive a quality score (0-100)
- **Required sections:** Validates all mandatory fields are completed
- **Placeholder detection:** Ensures placeholder text is replaced
- **Checkbox verification:** Confirms required agreements are checked

### 🕐 Lifecycle Management
- **Stale detection:** Issues inactive for 30 days are marked stale
- **Auto-closure:** Stale issues without activity are closed after 7 days
- **Exemptions:** Critical, security, and in-progress issues are protected
- **Welcome messages:** First-time contributors receive helpful guidance

## Template Enforcement

### Mandatory Usage
- **No blank issues:** Template usage is required for all new issues
- **Auto-validation:** Non-compliant issues are automatically flagged
- **Helpful guidance:** Users receive instructions to use proper templates
- **Quality feedback:** Issues get improvement suggestions

### Compliance Levels
- **🟢 Excellent (80-100):** Complete, well-documented issues
- **🟡 Good (60-79):** Adequate information, minor improvements needed
- **🟠 Needs Work (40-59):** Missing information, requires updates
- **🔴 Poor (0-39):** Incomplete, may be closed for template compliance

## Special Labels

### Automatic Labels
- `needs-template` - Issue doesn't use required template
- `needs-improvement` - Template compliance issues detected
- `needs-more-info` - Insufficient information provided
- `well-documented` - High-quality, complete issue report
- `ready-for-review` - Meets all requirements, ready for triage
- `good first issue` - Suitable for new contributors
- `stale` - No activity for extended period

### Priority Labels
- `priority: critical` - Immediate attention required
- `priority: high` - Important, address soon
- `priority: medium` - Standard priority
- `priority: low` - Nice to have, low urgency

### Effort Labels
- `effort: small` - Quick fix, 1-4 hours
- `effort: medium` - Moderate work, 1-3 days
- `effort: large` - Significant effort, 1-2 weeks
- `effort: extra-large` - Major undertaking, months

## Best Practices

### For Issue Reporters
1. **Choose the right template** - Select the template that best matches your issue type
2. **Complete all required fields** - Provide thorough, specific information
3. **Replace placeholder text** - Don't leave template examples unchanged
4. **Be specific** - Include exact error messages, steps, and environment details
5. **Add context** - Explain what you were trying to achieve
6. **Check existing issues** - Search for duplicates before creating new issues

### For Maintainers
1. **Review auto-labels** - Verify automated labeling is accurate
2. **Update priority** - Adjust priority based on project roadmap
3. **Request information** - Ask for missing details when needed
4. **Close duplicates** - Link to existing issues and close duplicates
5. **Thank contributors** - Acknowledge quality issue reports

## Configuration

### Template Customization
Templates are located in `.github/ISSUE_TEMPLATE/` and can be customized:
- **Fields:** Add, remove, or modify form fields
- **Labels:** Change default labels for each template
- **Validation:** Adjust required vs optional fields
- **Assignees:** Set default assignees for template types

### Workflow Configuration
Automation workflows in `.github/workflows/`:
- `issue-management.yml` - Core issue handling and labeling
- `issue-labeler.yml` - Advanced content-based labeling
- `stale-issues.yml` - Lifecycle management
- `template-validator.yml` - Template compliance checking

### Label Management
Recommended label structure:
```
Type: bug, enhancement, documentation, question
Priority: priority: critical/high/medium/low
Effort: effort: small/medium/large/extra-large
Status: needs-triage, in-progress, blocked, ready-for-review
Quality: well-documented, needs-more-info, needs-improvement
Special: good first issue, help wanted, duplicate, wontfix
```

## Troubleshooting

### Common Issues
- **Template not detected:** Ensure you're using the template form, not blank issue
- **Missing auto-labels:** Check if template title follows required format
- **Validation errors:** Complete all required fields and check required checkboxes
- **Stale marking:** Comment on issue to keep it active

### Getting Help
- Check existing issues and documentation first
- Use the Question/Help template for usage questions
- Contact maintainers for template system issues
- Review this guide for detailed information

## Examples

### Good Bug Report Title
`[Bug]: CSV export fails with special characters in filename`

### Good Feature Request Title
`[Feature]: Add support for custom CV templates`

### Good Documentation Title
`[Docs]: Installation guide missing Python version requirements`

### Good Question Title
`[Question]: How to configure custom output formats`

---

*This template system helps maintain high-quality issues and efficient project management. Thank you for following these guidelines!*