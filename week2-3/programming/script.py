'''week 1 ex'''
# score=[60,75,90,75]
# total = 0;
# for i in score:
#     total += i
# print("average score")
# average = total / len(score)
# print(average)
# print("score strictly above average")
# for i in score:
#     if i>average:
#         print(i)
# print("score above or equal to average")
# for i in score:
#     if i>=average:
#         print(i)
# for i, s in enumerate(score):
#     if s>average:
#         print("score of student", i, "is", s)
'''week 2 ex'''
# values = [int(x) for x in (input("Enter a list of numbers separated by space: ")).split()]
# threshold =int(input("Enter a threshold value: "))
# def select_at_least(values, threshold):
#     for i in values:
#         if i>threshold:
#             print(i)
# select_at_least(values, threshold)
# class ScoreRecords:
#     def __init__(self, rows):
#         self.rows = rows

#     def __len__(self):
#         return len(self.rows)

#     def __getitem__(self, index):
#         return self.rows[index]


# score_records = ScoreRecords([("Ada", 72), ("Bo", 86), ("Cai", 68)])
# name, score = score_records[1]
# print(name, score)
# def average(list):
#     total = 0
#     if not list: raise ValueError("List is empty")
#     for i in list:
#         total += i
#     return total / len(list)
# try:
#     average([])
# except ValueError as e:
#     print("Error:", e)
# except ZeroDivisionError as e:
#     print("Error:", e)
'''week 3 ex'''
# import torch as t
# x=t.tensor([[2.,4.,6.],[1.,3.,5.]])
# print(x[:,-1],tuple(x[:,-1].shape))
# print(x[:,-1:],tuple(x[:,-1:].shape))
# print(x.reshape(3,2))
# print(x.T)
# total = 0
# for i in range(2):
#     for j in range(3): 
#         total+=x[i,j]
#     print(total/3)
#     total=0
# print(x @ x.T)
'''week 4 ex'''

# import torch
# from torch.utils.data import Dataset, DataLoader
# from torchvision.transforms import v2
# from torch.nn import functional as F
# from torchvision import datasets
# train_data = datasets.FashionMNIST(root='data', train=True, download=False, transform=v2.ToTensor())
# test_data = datasets.FashionMNIST(root='data', train=False, download=False, transform=v2.ToTensor())
# loader = DataLoader(train_data, batch_size=16, shuffle=False)
# batch=next(iter(loader))
# print(batch[0].shape,batch[1].type)

# print(torch.equal(batch[0][0],train_data[0][0]))
# print((batch[1][0].item()==train_data[0][1]))


from torch.utils.data import DataLoader

nums = [10, 20, 30, 40, 50]

for drop_last in [False, True]:
    loader = DataLoader(nums, batch_size=2, shuffle=False, drop_last=drop_last)

    print(f"drop_last={drop_last}")
    for i, batch in enumerate(loader, start=1):
        print(f"第 {i} 批：{batch.tolist()}")
