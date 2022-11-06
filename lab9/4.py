class PrintAverage(Exception):
    pass


class PrintDispersion(Exception):
    pass


class PrintCount(Exception):
    pass


def data_cor():
    device_data = []
    try:
        while True:
            try:
                cur = yield
                device_data.append(cur)
            except PrintAverage:
                yield sum(device_data) / len(device_data)
            except PrintDispersion:
                avg = sum(device_data) / len(device_data)
                yield sum((i - avg) ** 2 for i in device_data) / (len(device_data) - 1)
            except PrintCount:
                yield len(device_data)
    finally:
         return
