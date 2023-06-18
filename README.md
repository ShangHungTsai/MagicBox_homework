# MagicBox homework
1. test.py
Try to read input from command.
```shell
python test.py
# Input integer sequence: 1 3 5
# Output: [1 3 5]
```

2. predict.py
Try to predict by diff.
```shell
python predict.py
# Input integer sequence: 3 5 7
# Output: 9 11 13 15 17 19 21 23 25 27
```

3. predict-linearRegression
Try to predict linearRegression with library.
```shell
cd ./predict-linearRegression
docker build -t predict .
docker run -it predict
# Input integer sequence
``