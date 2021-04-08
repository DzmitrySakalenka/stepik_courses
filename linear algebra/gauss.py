import numpy as np
import logging


tests = [
         np.array(
         [[6,  1,  2, 21],
          [4, -6, 16,  2],
          [3,  8,  1,  2]
         ], dtype=np.float64),
         np.array(
         [[5, -3,  2, -8, 1],
          [1,  1,  1,  1, 0],
          [3,  5,  1,  4, 0],
          [4,  2,  3,  1, 3]
         ], dtype=np.float64),
         np.array(
         [[1, 2, 3, 3],
          [3, 5, 7, 0],
          [1, 3, 4, 1]
         ], dtype=np.float64),
         np.array(
         [[2,  5, 4, 1, 20],
          [1,  3, 2, 1, 11],
          [2, 10, 9, 7, 40],
          [3,  8, 9, 2, 37]
         ], dtype=np.float64),
         np.array(
         [[1, -2,  1, 0],
          [2,  2, -1, 3],
          [4, -1,  1, 5]
         ], dtype=np.float64),
         np.array(
         [[3,   2,  1,  1, -2],
          [1,  -1,  4, -1, -1],
          [-2, -2, -3,  1,  9],
          [ 1,  5, -1,  2,  4]
         ], dtype=np.float64),
         np.array(
         [[0.12, 0.18, -0.17,   5.5],
          [0.06, 0.09,  0.15, -1.95],
          [0.22, -0.1,  0.06,   0.5]
         ], dtype=np.float64),
         np.array(
         [[2, -1,  3,  1],
          [2, -1, -1, -2],
          [4, -2,  6,  0],
          [6,  8, -7,  2]
         ], dtype=np.float64),
         np.array(
         [[1, 2, 1,  1,  3,  1,  7],
          [1, 2, 1,  2,  1, -1,  1],
          [1, 2, 1, -1,  5, -1,  2],
          [1, 2, 1, -2, -4, -4, -1]
         ], dtype=np.float64),
         np.array(
         [[3,  -2,  1, 0],
          [5, -14, 15, 0],
          [1,   2, -3, 0]
         ], dtype=np.float64),
         np.array(
         [[2,  3, -1,  1,  0],
          [2,  7, -3,  0,  1],
          [0,  4, -2, -1,  1],
          [2, -1,  1,  2, -1],
          [4, 10, -4,  1,  1]
         ], dtype=np.float64),
         np.array(
         [[3, -5,  2,  4, 2],
          [7, -4,  1,  3, 5],
          [5,  7, -4, -6, 3]
         ], dtype=np.float64),
         np.array(
         [[0,  2, -1, -4],
          [1, -1,  5,  3],
          [2,  1, -1,  0],
          [3,  2,  3, -1],
          [3,  4,  2, -5]
         ], dtype=np.float64)]
tests_answ = [
              np.array([4.13333333333333333333, -1.13333333333333333333, -1.33333333333333333333], dtype=np.float64),
              np.array([7, -8, -5, 6], dtype=np.float64),
              np.array([-4, -13, 11], dtype=np.float64),
              np.array([1, 2, 2, 0], dtype=np.float64),
              np.array([1, 2, 3], dtype=np.float64),
              np.array([-3, -1, 2, 7], dtype=np.float64),
              np.array([10, 5, -20], dtype=np.float64),
              np.array([0, 0, 0, 0], dtype=np.float64),
              np.array([0, 0, 0, 0, 0, 0], dtype=np.float64),
              np.array([0, 0, 0], dtype=np.float64),
              np.array([0, 0, 0, 0], dtype=np.float64),
              np.array([0, 0, 0, 0], dtype=np.float64),
              np.array([1, -2, 0], dtype=np.float64)
             ]


logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(message)s')


def gauss(a):
    logging.debug(f'input matrix: \n {a}')

    n = a.shape[0]
    m = a.shape[1] - 1
    
    where = np.full(m, -1)
    row = 0

    for col in range(m):
        if row >= n:
            break
        
        sel = np.argmax(np.abs(a[row:n, col]))+row

        if np.abs(a[sel, col]) < np.finfo(np.float32).eps:
            continue

        a[[sel, row]] = a[[row, sel]]
        where[col] = row

        logging.debug(f'matrix with pivoting on step {col}-{row}: \n {a}')

        no_i = [k for k in range(n) if k != row]
        c = a[no_i, col] / a[row, col]
        a[no_i, :] -= c[np.newaxis].T * a[row, :][np.newaxis]

        logging.debug(f'matrix on step {col}-{row}: \n {a}')

        row += 1
    
    logging.debug(f'final matrix: \n {a}')

    ans = np.full(m, 0.)
    no_i = [k for k in range(m) if where[k] != -1]
    ans[no_i] = a[where[no_i], m] / a[where[no_i], no_i]

    #logging.debug(f'final x-vector: \n {ans}')

    for i in range(n):
        sum = np.sum(ans*a[i, :m])

        if np.abs(sum - a[i, m]) > np.finfo(np.float32).eps:
            return 0, np.NaN
    
    if -1 in where:
        return np.Inf, np.NaN

    return 1, ans


def pretty_gauss():
    n, m = map(int, input().split())
    a = np.zeros((n, m+1))

    for i in range(n):
        a[i, :] = list(map(int, input().split()))
    
    tp, ans = gauss(a)

    if tp == 0:
        print("NO")
    elif tp == np.Inf:
        print("INF")
    else:
        ans = np.round(ans, 15)
        print('YES')
        print(' '.join(map(str, ans)))


def test_method():
    for i in range(len(tests)):
        print('Test #', i)
        print(gauss(tests[i]))
        print(f'True answer: \n {tests_answ[i]}')
        #np.testing.assert_equal(gauss(tests[i]).astype(np.int64), tests_answ[i].astype(np.int64))