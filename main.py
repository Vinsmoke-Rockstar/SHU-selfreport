import argparse

from utils import test_report, test_send_email, auto_report


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--test_report', '-r', action='store_true', help='测试账号是否正确')
    parser.add_argument('--test_send_email', '-e', action='store_true', help='测试邮件发送模块')
    parser.add_argument("--account", '-a', type=str, help="选择了测试邮件功能，使用该选项输入测试邮件收件邮箱")
    args = parser.parse_args()

    setting_config_path = 'setting_config.yaml'
    report_config_path = 'report_config.yaml'

    if args.test_report:
        test_report(report_config_path)

    if args.test_send_email:
        if args.account is None:
            print("邮件发送功能错误：请使用参数'--account'或'-a'输入收件邮箱")
        else:
            test_send_email(args.account, report_config_path)

    if args.test_report or args.test_send_email:
        exit(0)

    auto_report(report_config_path, setting_config_path)
