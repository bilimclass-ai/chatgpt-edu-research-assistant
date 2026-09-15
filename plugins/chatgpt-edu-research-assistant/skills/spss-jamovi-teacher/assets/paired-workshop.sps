* Original synthetic teaching data. Not empirical research findings.
* Open in a fresh teaching session after saving any current work.
* Reviewed against documentation; native execution must be checked locally.
NEW FILE.
DATA LIST FREE /id pre post.
BEGIN DATA
1 50 52
2 55 59
3 60 63
4 65 70
5 70 74
6 75 81
7 52 53
8 57 60
9 62 64
10 67 71
11 72 75
12 77 82
END DATA.
VARIABLE LABELS
 id 'Synthetic participant ID'
 pre 'Pre-workshop score, 0-100 points'
 post 'Post-workshop score, 0-100 points'.
VARIABLE LEVEL id (NOMINAL) pre post (SCALE).
COMPUTE change=post-pre.
VARIABLE LABELS change 'Change in points: post minus pre'.
DESCRIPTIVES VARIABLES=pre post change
 /STATISTICS=MEAN STDDEV MIN MAX.
T-TEST PAIRS=post WITH pre (PAIRED)
 /MISSING=ANALYSIS
 /CRITERIA=CI(.95).
