from utils.stream import IncrementalTaskStream, get_cls_order

task_stream = IncrementalTaskStream(
    data="har", scenario="class", cls_order=[0, 1, 3, 4, 5, 2], split="exp"
)

x_train, y_train, x_test, y_test, sub_train = task_stream.load_data()
print(x_train.shape)
