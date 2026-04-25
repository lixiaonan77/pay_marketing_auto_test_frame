#Excel工具类用于数据驱动
import openpyxl

class ExcelUtil:
    # 静态变量：excel默认sheet名
    sheet_name = "case"

    @staticmethod
    def read_excel(file_path):
        """
        完整版读取Excel
        1.自动跳过表头
        2.自动将每一行转为字典
        3.自动去除空格、处理空值
        4.最终返回：列表套字典，直接给pytest参数化使用
        """
        # 打开excel
        wb = openpyxl.load_workbook(file_path)
        # 指定工作表
        sheet = wb[ExcelUtil.sheet_name]

        # 1.获取表头（第一行作为key）
        titles = [cell.value for cell in sheet[1]]

        case_list = []

        # 2.遍历从第二行开始读取用例数据
        for row in sheet.iter_rows(min_row=2,values_only=True):
            case_dict = {}
            # 表头+每行数据一一对应
            for index,value in enumerate(row):
                key = titles[index]
                # 数据处理：空值转为空字符串、去除前后空格
                if value is None:
                    value = ""
                if isinstance(value,str):
                    value = value.strip()

                case_dict[key] = value
            case_list.append(case_dict)

        wb.close()
        # 返回标准：列表套字典格式
        return case_list
