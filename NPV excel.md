| Data        | Description                                                  |                              |
| ----------- | ------------------------------------------------------------ | ---------------------------- |
| 15-Feb-08   | Settlement date                                              |                              |
| 15-Nov-16   | Maturity date                                                |                              |
| 5.75%       | Percent coupon                                               |                              |
| 95.04287    | Price                                                        |                              |
| $100.00     | Redemption value                                             |                              |
| 2           | Frequency is semiannual  (see above)                         |                              |
| 0           | 30/360 basis (see above)                                     |                              |
| Formula     | Description (Result)                                         | Result                       |
| 0.065000007 | The yield, for the bond  with the terms above (0.065 or 6.5%) | =YIELD(A2,A3,A4,A5,A6,A7,A8) |



| Data     | Description                                                  |                     |
| -------- | ------------------------------------------------------------ | ------------------- |
| 0.015    | Annual discount rate.  This might represent the rate of inflation or the interest rate of a  competing investment. |                     |
| -1000    | Initial cost of  investment                                  |                     |
| 15       | Return from first year                                       |                     |
| 15       | Return from second year                                      |                     |
| 15       | Return from third year                                       |                     |
| 15       | Return from fourth year                                      |                     |
| 15       | Return from fifth year                                       |                     |
| 15       |                                                              |                     |
| 15       |                                                              |                     |
| 15       |                                                              |                     |
| 15       |                                                              |                     |
| 1000     |                                                              |                     |
| Formula  | Description                                                  | Result              |
| ($12.93) | Net present value of  this investment                        | =NPV(A2, A4:A13)+A3 |





| Data        | Description                                                  |
| ----------- | ------------------------------------------------------------ |
| 3/31/08     | Settlement date                                              |
| 5/29/08     | Maturity date                                                |
| $92.00      | Price per $100 face value                                    |
| Formula     | Description                                                  |
| 0.530582167 | The yield for the Treasury bill using the terms in A2,  A3, and A4 (0.0914, or 9.14%). |

=TBILLYIELD(A2,A3,A4)