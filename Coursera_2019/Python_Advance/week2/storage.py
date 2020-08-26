import argparse
import json
import os
import tempfile

pathToTempFileData = os.path.join(tempfile.gettempdir(), 'storage.data')
pathToCounterMonitor = os.path.join(tempfile.gettempdir(), 'counter.data')
counterMonitor = 0


def recCounterMonitor():
    if counterMonitor > 0:
        monitor("session closed, counter successfully recorded")
    with open(pathToCounterMonitor, 'w') as f2:
        f2.write(str(counterMonitor))


def readLastCounter():
    if os.path.exists(pathToCounterMonitor):
        with open(pathToCounterMonitor, 'r') as d_f:
            d_temp_str = (d_f.read())
            if d_temp_str == "":
                return 1
            else:
                return int(d_temp_str)
    else:
        return 1


def monitor(d_str, *param):
    global counterMonitor
    if counterMonitor > 0:
        print("[", counterMonitor, "]", sep="", end="")
        print(d_str, *param)
        counterMonitor += 1


def dismissKeysFromData():
    os.remove(pathToTempFileData)
    os.remove(pathToCounterMonitor)
    if counterMonitor > 0:
        monitor("keys dismissed")


def readData():
    if not os.path.exists(pathToTempFileData):
        return {}

    with open(pathToTempFileData, 'r') as f:
        raw_data = f.read()
        if raw_data:
            return json.loads(raw_data)
        return {}


def recordKeyToData(d_key, d_value):
    d_data = readData()
    monitor("data", d_data)
    if d_key in d_data:
        d_data[d_key].append(d_value)
        if counterMonitor > 0:
            monitor("key already in data")
            monitor("values of key after change", d_data[d_key])
            monitor("storage after change", d_data)

    else:
        d_data[d_key] = [d_value]
        if counterMonitor > 0:
            monitor("key not in data")
            monitor("values of key after change", d_data[d_key])
            monitor("storage after change", d_data)

    with open(pathToTempFileData, 'w') as f:
        f.write(json.dumps(d_data))


def showKeyInData(d_key):
    d_data = readData()
    result = d_data.get(d_key)
    if counterMonitor > 0:
        if result is None:
            monitor("no value in storage for presentation by key", d_key)
        else:
            monitor("values in storage for presentation by key", d_key, ":")
    return result


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--key', default=None, dest='key_name', help='Key')
    parser.add_argument('--val', default=None, dest='value', help='Value')
    parser.add_argument('--mon', action='store_true', dest='monitor',
                        help='Monitor')
    parser.add_argument('--dis', action='store_true', help='Dismiss')

    args = parser.parse_args()
    if args.monitor:
        counterMonitor = readLastCounter()
        monitor("args", args)
        monitor("type args", type(args))

    if args.dis:
        dismissKeysFromData()
    elif args.key_name and args.value:
        recordKeyToData(args.key_name, args.value)
    elif args.key_name:
        print(showKeyInData(args.key_name))
    else:
        print('Wrong command')

    if args.monitor and not args.dis:
        recCounterMonitor()
