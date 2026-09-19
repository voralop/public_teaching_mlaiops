# Lab 2 — Run comparison

Experiment `itcs355-lab2` · 12 trials · total spend 0.0000 THB

`thb_per_point` is cost per percentage point of val_roc_auc above the worst trial. Cheap improvements rank low; expensive improvements rank high, however good the headline number is.

| run_id   |   val_roc_auc |   cost_thb |   n_estimators |   max_depth |   min_samples_leaf |   thb_per_point |
|:---------|--------------:|-----------:|---------------:|------------:|-------------------:|----------------:|
| 0f7a8e39 |        0.8426 |          0 |            100 |           4 |                  5 |               0 |
| aee57d5d |        0.8424 |          0 |            100 |           4 |                  1 |               0 |
| a120bb1e |        0.8411 |          0 |            300 |           4 |                  5 |               0 |
| 34bcee10 |        0.8404 |          0 |            300 |           4 |                  1 |               0 |
| 89359292 |        0.8397 |          0 |            100 |           8 |                  5 |               0 |
| f1edc9b9 |        0.8377 |          0 |            300 |           8 |                  5 |               0 |
| 39628cc8 |        0.8354 |          0 |            300 |          12 |                  5 |               0 |
| a3b7a80f |        0.8338 |          0 |            300 |           8 |                  1 |               0 |
| e8b306e1 |        0.8322 |          0 |            100 |          12 |                  5 |               0 |
| 2568052d |        0.8312 |          0 |            100 |           8 |                  1 |               0 |
| 5ac8381d |        0.8268 |          0 |            100 |          12 |                  1 |               0 |
| 8fd58505 |        0.8265 |          0 |            300 |          12 |                  1 |               0 |

## Which model did you register, and why?

TODO(Lab 2): 200 words maximum. Must address all four:

1. Why this model rather than the highest-scoring one, if they differ
2. The variance across seeds for your chosen configuration
3. What it costs to train, and to retrain monthly
4. One way this choice could be wrong

An answer that only says "highest validation score" scores zero on this task.