from bs4 import BeautifulSoup
import imaplib
import email.header
import email

IMAPServer = {
    "qq" : "imap.qq.com",
    "163" : "imap.163.com",
    "outlook" : "imap.outlook.com",
    "126" : "imap.126.com"}

class IMAP:
    def __init__(self):
        self.user_id = input("Login:")
        self.password = input("Password:")
        self.imap_server = IMAPServer[input("Server:")]

    def login(self):
        """
        登录邮件服务器
        :param
        :return: imap连接
        """
        try:
            serv = imaplib.IMAP4_SSL(self.imap_server, 993)  # SSL加密
            print('imap4 服务器连接成功')
        except Exception as e:
            print('imap4 服务器连接失败:', e)
            exit(1)

        try:
            serv.login(self.user_id, self.password)
            print('imap4 登录成功')
            return serv
        except Exception as e:
            print('imap4 登录失败：', e)
            exit(1)

    def loginout(self, conn):
        """
        登出邮件服务器
        :param conn: imap连接
        :return:
        """
        conn.close
        conn.logout()

    def get_content(self, conn):
        """
        获取指定邮件，解析内容
        :param conn: imap连接
        :return:
        """
        # 在连接服务器后，搜索之前，需要选择邮箱，默认select(mailbox='INBOX', readonly=False)
        conn.select()
        # 筛选符合条件的邮件，这里不知道怎么过滤复杂条件，只能过滤未读邮件或全部
        # ret, data = conn.search(None, 'UNSEEN')  # 未读邮件
        # ret, data = conn.search(None, '(FROM "qq814701082@163.com")')
        ret, data = conn.search(None, 'ALL')  # 所有邮件
        # 邮件列表
        email_list = data[0].split()
        if len(email_list) == 0:
            print('收件箱为空，已退出')
            exit(1)
        # 获取最后一封邮件的序号
        item = email_list[len(email_list) - 1]
        # 获取最后一封邮件内容
        ret, data = conn.fetch(item, '(RFC822)')
        msg = email.message_from_string(data[0][1].decode('gbk'))
        sub = msg.get('subject')
        email_from = msg.get('from')
        email_to = msg.get('to')
        sub_text = email.header.decode_header(sub)
        email_from_text = email.header.decode_header(email_from)
        email_to_text = email.header.decode_header(email_to)
        # 如果是特殊字符，元组的第二位会给出编码格式，需要转码
        if sub_text[0]:
            sub_detail = self.tuple_to_str(sub_text[0])
        email_from_detail = ''
        for i in range(len(email_from_text)):
            email_from_detail = email_from_detail + \
                self.tuple_to_str(email_from_text[i])
        email_to_detail = ''
        for i in range(len(email_to_text)):
            email_to_detail = email_to_detail + \
                self.tuple_to_str(email_to_text[i])

        print('主题：', sub_detail)
        print('发件人：', email_from_detail)
        print('收件人：', email_to_detail)
        # 通过walk可以遍历出所有的内容
        for part in msg.walk():
            # 这里要判断是否是multipart，如果是，数据没用丢弃
            if not part.is_multipart():
                # 字符集
                # charset = part.get_charset()
                # print('charset: ', charset)
                # 内容类型
                content_type = part.get_content_type()
                # print('content-type', content_type)
                # 如果是附件，这里就会取出附件的文件名，以下两种方式都可以获取
                # name = part.get_param("name")
                name = part.get_filename()
                if name:
                    # 附件
                    # 中文名获取到的是=?GBK?Q?=D6=D0=CE=C4=C3=FB.docx?=(中文名.docx)格式，需要将其解码为bytes格式
                    trans_name = email.header.decode_header(name)
                    if trans_name[0][1]:
                        # 将bytes格式转为可读格式
                        file_name = trans_name[0][0].decode(trans_name[0][1])
                    else:
                        file_name = trans_name[0][0]
                    print('开始下载附件:', file_name)
                    attach_data = part.get_payload(
                        decode=True)  # 解码出附件数据，然后存储到文件中
                    try:
                        # 注意一定要用wb来打开文件，因为附件一般都是二进制文件
                        f = open(file_name, 'wb')
                    except Exception as e:
                        print(e)
                        f = open('tmp', 'wb')
                    f.write(attach_data)
                    f.close()
                    print('附件下载成功:', file_name)
                else:
                    # 文本内容
                    txt = part.get_payload(decode=True)  # 解码文本内容
                    # 分别解释text/html和text/plain两种类型，纯文本解释起来较简单，两种类型内容一致
                    if content_type == 'text/html':
                        print('以下是邮件正文(text/html)：')
                        # 这里笔者不同邮件服务器遇到了不同情况，只解释了QQ邮箱，163的可以修改代码：
                        # QQ邮箱
                        # 1、有两层<div>标签，格式为<html><body><div><div>文本1</div><div>文本2</div></div></body></html>
                        # 2、只有一层<div>标签，格式为<html><body><div><p>文本1</p><p>文本2</p></div></body></html>
                        # 163邮箱
                        # 只有一层<div>标签，格式为<html><head><meta/></head><body><div>文本1</div><div>文本2</div></body></html>
                        soup = BeautifulSoup(str(txt, 'gbk'), 'lxml')
                        div_data = soup.find_all('div')
                        if len(div_data) > 1:
                            for each in div_data[1:]:
                                print(each.text)
                        else:
                            for each in soup.find_all('p'):
                                print(each.text)
                    elif content_type == 'text/plain':
                        print('以下是邮件正文(text/plain)：')
                        # 纯文本格式为bytes，不同邮件服务器较统一
                        print(str(txt, 'gbk'))

    def front(self, conn):
        """
        使用163邮箱，必须在select之前上传客户端身份信息,否则报错：command SEARCH illegal in state AUTH, only allowed in states SELECTED
        :param conn: imap连接
        :return:
        """
        imaplib.Commands['ID'] = 'AUTH'
        # 如果使用163邮箱，需要上传客户端身份信息
        args = ("name", "XXXX", "contact", "XXXX@163.com",
                "version", "1.0.0", "vendor", "myclient")
        typ, dat = conn._simple_command('ID', '("' + '" "'.join(args) + '")')
        # print(conn._untagged_response(typ, dat, 'ID'))

    def tuple_to_str(self, tuple_):
        """
        :param tuple_: 转换前的元组，QQ邮箱格式为(b'\xcd\xf5\xd4\xc6', 'gbk')或者(b' <XXXX@163.com>', None)，163邮箱格式为('<XXXX@163.com>', None)
        :return: 转换后的字符串
        """
        if tuple_[1]:
            out_str = tuple_[0].decode(tuple_[1])
        else:
            if isinstance(tuple_[0], bytes):
                out_str = tuple_[0].decode('gbk')
            else:
                out_str = tuple_[0]
        return out_str


def main():
    im = IMAP()
    conn = IMAP.login()
    im.front(conn)
    im.get_content(conn)
    im.loginout(conn)
