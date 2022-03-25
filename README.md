# Deep Summarization NLP

In Deep learning NLP, using a model we are trying to **summarization** the text.

## Using

```
$ python app.py
{'input_ids': tensor([[  222, 10045,   108,   114,  1482,   344,   117,   142,  3160,   113,
           114,   344,   327,   120,  1733,   109,   440,  1586,   111,   114,
           739,  3160, 68453,   532,   108,   568,   109, 23347,  1451,   108,
           111,  8133,   109, 10635,   532,   522,  3092,   110,   105,  2192,
          5612,   108,   290,  1482,   344,   137,   129,  4470,   115,   109,
           515,   114,  1877,  6989,   108,   241,   114,   111,  3027,   127,
           440,  1586,   107,  2110,   220,   440,   344, 29838,   109,   607,
         10635,   108,   532,   140,   568,   142, 23347,   344,   141, 54508,
         10833, 23425,   772,   107,   321,   109,  1482,   344,   114,  1877,
          6989,   108,   114,   117,   568,   109,   440,   297,   111,  3027,
           117,   568,   109, 23347,   297,   107,     1]]), 'attention_mask': tensor([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]])}
```

## Test

### Input
| Input | Output |
| --------------------- | -------------------- |
| In mathematics, a complex number is an element of a number system that contains the real numbers and a specific element denoted i, called the imaginary unit, and satisfying the equation i2 = −1. Moreover, every complex number can be expressed in the form a + bi, where a and b are real numbers. Because no real number satisfies the above equation, i was called an imaginary number by René Descartes. For the complex number a + bi, a is called the real part and b is called the imaginary part. | A complex number is an element of a number system that contains the real numbers and a specific element denoted i, called the imaginary unit, and satisfying the equation i2 =  ⁇ 1. |
| GitHub, Inc. is a provider of Internet hosting for software development and version control using Git. It offers the distributed version control and source code management functionality of Git, plus its own features. | GitHub is an open source software development platform. |
| GitLab Inc. is the open-core company that provides GitLab, the DevOps software that combines the ability to develop, secure, and operate software in a single application. The open source software project was created by Ukrainian developer Dmitriy Zaporozhets and Dutch developer Sytse Sijbrandij. | GitLab Inc. |
| Git is software for tracking changes in any set of files, usually used for coordinating work among programmers collaboratively developing source code during software development. Its goals include speed, data integrity, and support for distributed, non-linear workflows. | Git is an open-source software project developed by the Massachusetts Institute of Technology (MIT). |

## Sources

- https://github.com/google/sentencepiece#installation
- https://www.youtube.com/watch?v=Yo5Hw8aV3vY
