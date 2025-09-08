## Job Applicant Scoring System and Bias Analysis

This repository includes a transparent rule-based scoring function for applicants and a basic fairness audit.

### Scoring logic
- **Inputs**: `education`, `experience_years`, `gender`, `age`
- **Policy**: Sensitive attributes (`gender`, `age`) do not directly affect the score.
- **Education points**:
  - none: 0, highschool: 5, bachelors: 10, masters: 15, phd: 18
- **Experience**: 2 points per year up to 10 years, then 1 point per year beyond 10.
- **Score range**: Soft-capped to [0, 100].

### Why exclude gender and age?
- To reduce the risk of direct discrimination. These attributes are used only for auditing group-level outcomes (fairness checks).

### CLI usage
```bash
# Score one applicant (JSON via stdin)
echo '{"education":"masters","experience_years":5,"gender":"female","age":29}' | \
python task_4(cursor).py score

# Run a small synthetic audit
python task_4(cursor).py audit

# Run tests
python task_4(cursor).py --test
```

### Bias analysis
- We compute average scores per group for:
  - **Gender**: female, male, nonbinary, unspecified
  - **Age buckets**: <25, 25-34, 35-44, 45-54, 55+
- We report a simple **Disparate Impact Ratio (DIR)** per group relative to the highest-scoring group:
  - DIR(group) = avg_score(group) / avg_score(reference_group)
  - A common practical threshold is **0.8**: DIR < 0.8 may indicate disparity needing deeper investigation.

### Interpreting results and next steps
- If you see low DIR for any group, consider:
  - Reviewing feature choices (e.g., alternative education or experience measures)
  - Checking for proxy variables that correlate with sensitive attributes
  - Adding oversight and appeals processes
  - Considering more formal tests (e.g., regression analysis controlling for qualifications)

### File
- `task_4(cursor).py`: Scoring function, bias audit, CLI.


