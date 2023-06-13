import yaml


def read_yaml(self, path):
    with open(path, encoding="utf-8") as f:
        result = f.read()
        # result = yaml.load(result, Loader=yaml.FullLoader)
        # 语法糖转换
        result = yaml.full_load(result)
        result = yaml.load(result,loader=yaml.SafeLoader)
        return result

def write_yaml(self,path,data):
    with open(path,"w",encoding="utf-8") as f:
        yaml.dump(data,f,Dumper=yaml.SafeDumper)

    with open(path,encoding="utf-8") as f:
        result = f.read()
        result = yaml.safe_load(result)
        return result

