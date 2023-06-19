# 一、HTTP 介绍

HTTP协议是Hyper Text Transfer Protocol（超文本传输协议）的缩写,是用于从万维网（WWW:World Wide Web ）服务器传输超文本到本地浏览器的传送协议。

HTTP是一个基于TCP/IP通信协议来传递数据（HTML 文件, 图片文件, 查询结果等）。

### 1、HTTP 工作原理

HTTP协议工作于客户端-服务端架构上。浏览器作为HTTP客户端通过URL向HTTP服务端即WEB服务器发送所有请求。

Web服务器有：Nginx，Apache服务器，IIS服务器（Internet Information Services）等。

Web服务器根据接收到的请求后，向客户端发送响应信息。

HTTP默认端口号为80，但是你也可以改为8080或者其他端口。

**HTTP三点注意事项：**

- HTTP是无连接：无连接的含义是限制每次连接只处理一个请求。服务器处理完客户的请求，并收到客户的应答后，即断开连接。采用这种方式可以节省传输时间。
- HTTP是媒体独立的：这意味着，只要客户端和服务器知道如何处理的数据内容，任何类型的数据都可以通过HTTP发送。客户端以及服务器指定使用适合的MIME-type内容类型。
- HTTP是无状态：HTTP协议是无状态协议。无状态是指协议对于事务处理没有记忆能力。缺少状态意味着如果后续处理需要前面的信息，则它必须重传，这样可能导致每次连接传送的数据量增大。另一方面，在服务器不需要先前信息时它的应答就较快。

### 2、HTTP 消息结构

HTTP是基于客户端/服务端（C/S）的架构模型，通过一个可靠的链接来交换信息，是一个无状态的请求/响应协议。

一个HTTP"客户端"是一个应用程序（Web浏览器或其他任何客户端），通过连接到服务器达到向服务器发送一个或多个HTTP的请求的目的。

一个HTTP"服务器"同样也是一个应用程序（通常是一个Web服务，如Apache Web服务器或IIS服务器等），通过接收客户端的请求并向客户端发送HTTP响应数据。

HTTP使用统一资源标识符（Uniform Resource Identifiers, URI）来传输数据和建立连接。

### 3、客户端请求消息

客户端发送一个HTTP请求到服务器的请求消息包括以下格式：请求行（request line）、请求头部（header）、空行和请求数据四个部分组成

### 4、服务器响应消息

HTTP响应也由四个部分组成，分别是：状态行、消息报头、空行和响应正文。

**实例**

下面实例是一点典型的使用GET来传递数据的实例：

客户端请求：

```Bash
Connected to www.testpm.cn (47.244.247.240) port 80 (#0)
> GET /hello.txt HTTP/1.1   # 请求方式与版本协议。
> User-Agent: curl/7.29.0   #用什么客户端访问
> Host: www.testpm.cn  #主机名，域名。主机和端口号，
> Accept: */*  #匹配什么文件类型，“*” 是通用匹配。匹配所有类型
```

服务端响应:

```Bash
< HTTP/1.1 200 OK       #请求返回的状态码
< Server: nginx/1.16.0  #请求的服务和版本号
< Date: Thu, 04 Jul 2019 08:19:40 GMT
< Content-Type: text/plain #文本类型，有html，plain:普通文本
< Content-Length: 12
< Last-Modified: Thu, 04 Jul 2019 08:13:25 GMT
< Connection: keep-alive  #是否支持长连接
< ETag: "5d1db525-c"  #标识，每次访问如果与最开始的一样返回304否则校验不一致返回200
< Accept-Ranges: bytes
```

输出结果:

```Bash
hello world
```

### 5、HTTP 请求方法

根据HTTP标准，HTTP请求可以使用多种请求方法。

HTTP1.0定义了三种请求方法： GET, POST 和 HEAD方法。

HTTP1.1新增了五种请求方法：OPTIONS, PUT, DELETE, TRACE 和 CONNECT 方法。

# 二、HTTPS 协议介绍

- HTTP 协议（HyperText Transfer Protocol，超文本传输协议）：是客户端浏览器或其他程序与Web服务器之间的应用层通信协议 。
- HTTPS 协议（HyperText Transfer Protocol over Secure Socket Layer）：可以理解为HTTP+SSL/TLS， 即 HTTP 下加入 SSL 层，HTTPS 的安全基础是 SSL，因此加密的详细内容就需要 SSL，用于安全的 HTTP 数据传输。
- 如上图所示 HTTPS 相比 HTTP 多了一层 SSL/TLS
**SSL/TLS :SSL(Secure Sockets Layer 安全套接层),及其继任者传输层安全（Transport Layer Security，TLS）是为网络通信提供安全及数据完整性的一种安全协议。TLS与SSL在传输层为数据通讯进行加密提供安全支持。**

​           **SSL协议可分为两层：** SSL握手协议（SSL Handshake Protocol）：它建立在SSL记录协议之上，用于在实际的数据传输开始前，通讯双方进行身份认证、协商加密算法、交换加密密钥等。**相当于连接**

​    SSL记录协议（SSL Record Protocol）：它建立在可靠的传输协议（如TCP）之上，为高层协议提供数据封装、压缩、加密等基本功能的支持。 **相当于通信**

**SSL协议提供的服务主要有：**

ssl:身份认证和数据加密。保证数据完整性
1）认证用户和服务器，确保数据发送到正确的客户机和服务器；

2）加密数据以防止数据中途被窃取；

3）维护数据的完整性，确保数据在传输过程中不被改变。

### 1、HTTP 访问过程

如上图所示，HTTP请求过程中，客户端与服务器之间没有任何身份确认的过程，数据全部明文传输，“裸奔”在互联网上，所以很容易遭到黑客的攻击，如下：

可以看到，客户端发出的请求很容易被黑客截获，如果此时黑客冒充服务器，则其可返回任意信息给客户端，而不被客户端察觉。

**所以 HTTP 传输面临的风险有：**

- 窃听风险：黑客可以获知通信内容。
- 篡改风险：黑客可以修改通信内容。
- 冒充风险：黑客可以冒充他人身份参与通信。

那有没有一种方式既可以安全的获取公钥，又能防止黑客冒充呢？ 那就需要用到终极武器了：SSL 证书（申购）

- 证书：.crt, .pem
- 私钥：.key
- 证书请求文件：.csr

在第 ② 步时服务器发送了一个SSL证书给客户端，SSL 证书中包含的具体内容有：

（1）证书的发布机构CA

（2）证书的有效期

（3）公钥

（4）证书所有者

（5）签名   -----   签名就可以理解为是钞票里面的一个防伪标签。

**客户端在接受到服务端发来的SSL证书时，会对证书的真伪进行校验，以浏览器为例说明如下：**

（1）首先浏览器读取证书中的证书所有者、有效期等信息进行一一校验

（2）浏览器开始查找操作系统中已内置的受信任的证书发布机构CA，与服务器发来的证书中的颁发者CA比对，用于校验证书是否为合法机构颁发

（3）如果找不到，浏览器就会报错，说明服务器发来的证书是不可信任的。

（4）如果找到，那么浏览器就会从操作系统中取出 颁发者CA 的公钥，然后对服务器发来的证书里面的签名进行解密

（5）浏览器使用相同的hash算法计算出服务器发来的证书的hash值，将这个计算的hash值与证书中签名做对比

（6）对比结果一致，则证明服务器发来的证书合法，没有被冒充

（7）此时浏览器就可以读取证书中的公钥，用于后续加密了

(8）client与web协商对称加密算法，client生成对称加密密钥并使用web公钥加密，发送给web服务器，web服务器使用web私钥解密

(9)使用对称加密密钥传输数据，并校验数据的完整性

4、所以通过发送SSL证书的形式，既解决了公钥获取问题，又解决了黑客冒充问题，一箭双雕，HTTPS加密过程也就此形成

**所以相比HTTP，HTTPS 传输更加安全**

（1） 所有信息都是加密传播，黑客无法窃听。

（2） 具有校验机制，一旦被篡改，通信双方会立刻发现。

（3） 配备身份证书，防止身份被冒充。

### 2、HTTPS 总结

**综上所述，相比 HTTP 协议，HTTPS 协议增加了很多握手、加密解密等流程，虽然过程很复杂，但其可以保证数据传输的安全。**

HTTPS 缺点：

1. SSL 证书费用很高，以及其在服务器上的部署、更新维护非常繁琐
2. HTTPS 降低用户访问速度（多次握手）
3. 网站改用HTTPS 以后，由HTTP 跳转到 HTTPS 的方式增加了用户访问耗时（多数网站采用302跳转）
4. HTTPS 涉及到的安全算法会消耗 CPU 资源，需要增加大量机器（https访问过程需要加解密）

### 3、构建私有的 CA 机构

====================================================================

CA中心申请证书的流程:

过程：
1。web服务器,生成一对非对称加密密钥（web公钥，web私钥）
2。web服务器使用 web私钥 生成 web服务器的证书请求，并将证书请求发给CA服务器
3。CA服务器使用 CA的私钥 对 web 服务器的证书请求 进行数字签名得到 web服务器的数字证书，并将web服务器的数字证书颁发给web服务器。
4。client访问web服务器，请求https连接，下载web数字证书
5。client下载 CA数字证书（CA身份信息＋CA公钥，由上一级CA颁发，也可自签名颁发），验证 web数字证书（CA数字证书中有CA公钥，web数字证书是使用CA私钥签名的）

#### 1、CA 介绍

CA（Certificate Authority）证书颁发机构主要负责证书的颁发、管理以及归档和吊销。证书内包含了拥有证书者的姓名、地址、电子邮件帐号、公钥、证书有效期、发放证书的CA、CA的数字签名等信息。**证书主要有三大功能：加密、签名、身份验证。**

#### 2、构建私有 CA

#### 1、检查安装 openssl

```Bash
[root@https-ca ~]# rpm -qa openssl
```

如果未安装

```Bash
[root@https-ca ~]# yum install openssl openssl-devel
```

#### 2、查看配置文件

openssl 配置`/etc/pki/tls/openssl.cnf`有关CA的配置。如果服务器为证书签署者的身份那么就会用到此配置文件，此配置文件对于证书申请者是无作用的。

```Bash
[root@https-ca ~]# vim /etc/pki/tls/openssl.cnf
####################################################################
[ ca ]
default_ca      = CA_default            # 默认的CA配置；CA_default指向下面配置块

####################################################################
[ CA_default ]

dir             = /etc/pki/CA           # CA的默认工作目录
certs           = $dir/certs            # 认证证书的目录
crl_dir         = $dir/crl              # 证书吊销列表的路径
database        = $dir/index.txt        # 数据库的索引文件


new_certs_dir   = $dir/newcerts         # 新颁发证书的默认路径

certificate     = $dir/cacert.pem       # 此服务认证证书，如果此服务器为根CA那么这里为自颁发证书
serial          = $dir/serial           # 下一个证书的证书编号
crlnumber       = $dir/crlnumber        # 下一个吊销的证书编号
                                        
crl             = $dir/crl.pem          # The current CRL
private_key     = $dir/private/cakey.pem# CA的私钥
RANDFILE        = $dir/private/.rand    # 随机数文件

x509_extensions = usr_cert              # The extentions to add to the cert

name_opt        = ca_default            # 命名方式，以ca_default定义为准
cert_opt        = ca_default            # 证书参数，以ca_default定义为准


default_days    = 365                   # 证书默认有效期
default_crl_days= 30                    # CRl的有效期
default_md      = sha256                # 加密算法
preserve        = no                    # keep passed DN ordering


policy          = policy_match          #policy_match策略生效

# For the CA policy
[ policy_match ]
countryName             = match         #国家；match表示申请者的申请信息必须与此一致
stateOrProvinceName     = match         #州、省
organizationName        = match         #组织名、公司名
organizationalUnitName  = optional      #部门名称；optional表示申请者可以的信息与此可以不一致
commonName              = supplied
emailAddress            = optional

# For the 'anything' policy
# At this point in time, you must list all acceptable 'object'
# types.
[ policy_anything ]                     #由于定义了policy_match策略生效，所以此策略暂未生效
countryName             = optional
stateOrProvinceName     = optional
localityName            = optional
organizationName        = optional
organizationalUnitName  = optional
commonName              = supplied
emailAddress            = optional
```

#### 3、根证书服务器目录

根CA服务器：因为只有 CA 服务器的角色，所以用到的目录只有/etc/pki/CA

网站服务器：只是证书申请者的角色，所以用到的目录只有`/etc/pki/tls`

**4、创建所需要的文件**

```Bash
[root@https-ca ~]# cd /etc/pki/CA/
[root@https-ca CA]# ls
certs  crl  newcerts  private
[root@https-ca CA]# touch index.txt   #创建生成证书索引数据库文件
[root@https-ca CA]# ls
certs  crl  index.txt  newcerts  private
[root@https-ca CA]# echo 01 > serial   #指定第一个颁发证书的序列号
[root@https-ca CA]# ls
certs  crl  index.txt  newcerts  private  serial
[root@https-ca CA]# 
```

#### 5、创建密钥

在根CA服务器上创建密钥，密钥的位置必须为`/etc/pki/CA/private/cakey.pem`，这个是openssl.cnf中中指定的路径，只要与配置文件中指定的匹配即可。

```Bash
[root@https-ca CA]# (umask 066; openssl genrsa -out private/cakey.pem 2048)
Generating RSA private key, 2048 bit long modulus
...........+++
...............+++
e is 65537 (0x10001)
```

#### 6、生成自签名证书

根CA自签名证书，根CA是最顶级的认证机构，没有人能够认证他，所以只能自己认证自己生成自签名证书。

```Bash
[root@https-ca CA]# openssl req -new -x509 -key /etc/pki/CA/private/cakey.pem -days 7300 -out /etc/pki/CA/cacert.pem -days 7300
You are about to be asked to enter information that will be incorporated
into your certificate request.
What you are about to enter is what is called a Distinguished Name or a DN.
There are quite a few fields but you can leave some blank
For some fields there will be a default value,
If you enter '.', the field will be left blank.
-----
Country Name (2 letter code) [XX]:CN
State or Province Name (full name) []:BEIJING
Locality Name (eg, city) [Default City]:BEIJING
Organization Name (eg, company) [Default Company Ltd]:CA
Organizational Unit Name (eg, section) []:OPT
Common Name (eg, your name or your server's hostname) []:ca.qf.com
Email Address []:
[root@https-ca CA]# ls
cacert.pem  certs  crl  index.txt  newcerts  private  serial
```

```Bash
-new:   生成新证书签署请求
-x509:   专用于CA生成自签证书
-key:   生成请求时用到的私钥文件
-days n：  证书的有效期限
-out /PATH/TO/SOMECERTFILE:   证书的保存路径
```

#### 7、下载安装证书

`/etc/pki/CA/cacert.pem`就是生成的自签名证书文件，使用 `SZ/xftp `工具将他导出到窗口机器中。然后双击安装此证书到受信任的根证书颁发机构

```Bash
[root@https-ca CA]# yum install -y lrzsz
[root@https-ca CA]# sz cacert.pem
```

#### **8、客户端CA 证书申请及签名**

1、检查安装 openssl**

```Bash
[root@nginx-server ~]# rpm -qa openssl
```

如果未安装，安装 openssl

```Bash
[root@nginx-server ~]# yum install openssl openssl-devel
```

2、客户端生成私钥文件**

```Bash
[root@nginx-server ~]# (umask 066; openssl genrsa -out /etc/pki/tls/private/www.qf.com.key 2048)
Generating RSA private key, 2048 bit long modulus
..............................+++
..........+++
e is 65537 (0x10001)
[root@nginx-server ~]# cd /etc/pki/tls/private/
[root@nginx-server private]# ls
www.qf.com.key
[root@nginx-server private]#
```

3、客户端用私钥加密生成证书请求**

```Bash
[root@nginx-server private]# ls ../
cert.pem  certs  misc  openssl.cnf  private
[root@nginx-server private]# openssl req -new -key /etc/pki/tls/private/www.qf.com.key -days 365 -out /etc/pki/tls/www.qf.com.csr
You are about to be asked to enter information that will be incorporated
into your certificate request.
What you are about to enter is what is called a Distinguished Name or a DN.
There are quite a few fields but you can leave some blank
For some fields there will be a default value,
If you enter '.', the field will be left blank.
-----
Country Name (2 letter code) [XX]:CN
State or Province Name (full name) []:BEIJING
Locality Name (eg, city) [Default City]:BEIJING
Organization Name (eg, company) [Default Company Ltd]:QF
Organizational Unit Name (eg, section) []:OPT
Common Name (eg, your name or your server's hostname) []:www.qf.com
Email Address []:

Please enter the following 'extra' attributes
to be sent with your certificate request
A challenge password []:
An optional company name []:
[root@nginx-server private]# ls ../
cert.pem  certs  misc  openssl.cnf  private  www.qf.com.csr
[root@nginx-server private]#
```

CSR(Certificate Signing Request)包含了公钥和名字信息。通常以.csr为后缀，是网站向CA发起认证请求的文件，是中间文件。

在这一命令执行的过程中，系统会要求填写如下信息：

最后把生成的请求文件（`/etc/pki/tls/www.qf.com.csr`）传输给CA ,这里我使用scp命令，通过ssh协议，将该文件传输到CA下的`/etc/pki/CA/private/`目录

```Bash
[root@nginx-server private]# cd ../
[root@nginx-server tls]# scp www.qf.com.csr 10.0.105.181:/etc/pki/CA/private
root@10.0.105.181's password: 
www.qf.com.csr                                                           100%  997   331.9KB/s   00:00 
```

**4、CA 签署证书**

```Bash
[root@https-ca ~]# openssl ca -in /etc/pki/CA/private/www.qf.com.csr -out /etc/pki/CA/certs/www.qf.com.crt -days 365
Using configuration from /etc/pki/tls/openssl.cnf
Check that the request matches the signature
Signature ok
Certificate Details:
        Serial Number: 1 (0x1)
        Validity
            Not Before: Jul  3 10:12:23 2019 GMT
            Not After : Jul  2 10:12:23 2020 GMT
        Subject:
            countryName               = CN
            stateOrProvinceName       = BEIJING
            organizationName          = QF
            organizationalUnitName    = OPT
            commonName                = www.qf.com
        X509v3 extensions:
            X509v3 Basic Constraints: 
                CA:FALSE
            Netscape Comment: 
                OpenSSL Generated Certificate
            X509v3 Subject Key Identifier: 
                E3:AC:1A:55:2B:28:B9:80:DC:9C:C2:13:70:53:27:AD:3D:44:8F:D3
            X509v3 Authority Key Identifier: 
                keyid:5D:2A:81:B2:E7:8D:D8:88:E5:7B:94:CA:75:65:9C:82:2B:A9:B2:3C

Certificate is to be certified until Jul  2 10:12:23 2020 GMT (365 days)
Sign the certificate? [y/n]:y


1 out of 1 certificate requests certified, commit? [y/n]y
Write out database with 1 new entries
Data Base Updated
```

证书通常以.crt为后缀，表示证书文件

**1、可能遇到的问题**

```Bash
[root@https-ca private]# cd
[root@https-ca ~]# openssl ca -in /etc/pki/CA/private/www.qf.com.csr -out /etc/pki/CA/certs/www.qf.com.ctr -days 365
Using configuration from /etc/pki/tls/openssl.cnf
Check that the request matches the signature
Signature ok
The organizationName field needed to be the same in the
CA certificate (CA) and the request (QF)
```

因为默认使用/etc/pki/tls/openssl.cnf，里面要求其一致，修改organizationName=supplied

修改 /etc/pki/tls/openssl.cnf

```Bash
[root@https-ca ~]# vim /etc/pki/tls/openssl.cnf
policy          = policy_match
 82 
 83 # For the CA policy
 84 [ policy_match ]
 85 countryName             = match
 86 stateOrProvinceName     = match
 87 organizationName        = supplied
 88 organizationalUnitName  = optional
 89 commonName              = supplied
 90 emailAddress            = optional
```

**2、查看生成的证书的信息**

```Bash
[root@https-ca ~]# openssl x509 -in /etc/pki/CA/certs/www.qf.com.crt -noout -subject
subject= /C=CN/ST=BEIJING/O=QF/OU=OPT/CN=www.qf.com
```

**3、将生成的证书发放给请求客户端**

```Bash
[root@https-ca ~]# cd /etc/pki/CA/certs/
[root@https-ca certs]# scp www.qf.com.ctr 10.0.105.199:/etc/pki/CA/certs/
root@10.0.105.199's password: 
www.qf.com.ctr                                                           100% 4422   998.3KB/s   00:00 
```

测试:

```Bash
在nginx-server端操作：
[root@localhost ~]# cd /etc/pki/
[root@localhost pki]# ls
CA  ca-trust  java  nssdb  nss-legacy  rpm-gpg  rsyslog  tls
[root@localhost pki]# cd CA/
[root@localhost CA]# ls
certs  crl  newcerts  private
[root@localhost CA]# cd certs/
[root@localhost certs]# ls
www.qf.com.crt
[root@localhost certs]# pwd
/etc/pki/CA/certs
[root@localhost certs]# ls
www.qf.com.ctr
[root@localhost certs]# pwd
/etc/pki/CA/certs
[root@localhost certs]# find / -name *.key
/etc/pki/tls/private/www.qf.com.key
/usr/share/doc/openssh-7.4p1/PROTOCOL.key
[root@localhost certs]# find / -name *.ctr

还是在这台机器安装nginx并且配置证书:
root@localhost conf.d]# pwd
/etc/nginx/conf.d
[root@localhost conf.d]# vim nginx.conf
server {
        listen       443 ssl;
        server_name  localhost;

        ssl_certificate         /etc/pki/CA/certs/www.qf.com.crt;  #指定证书路径
        ssl_certificate_key  /etc/pki/tls/private/www.qf.com.key;  #指定私钥路径
        ssl_session_timeout  5m;   #配置用于SSL会话的缓存
        ssl_protocols  SSLv2 SSLv3 TLSv1;   #指定使用的协议
        ssl_ciphers  ALL:!ADH:!EXPORT56:RC4+RSA:+HIGH:+MEDIUM:+LOW:+SSLv2:+EXP; # //密码指定为OpenSSL支持的格式
        ssl_prefer_server_ciphers   on;  #设置协商加密算法时，优先使用服务端的加密，而不是客户端浏览器的。

        location / {
                root /usr/share/nginx/html;
                index index.html index.htm;
                }
}
保存重启
[root@localhost conf.d]# nginx -t 
[root@localhost conf.d]# nginx -s reload
```

**4、CA吊销证书**

**1、知道客户端吊销的证书的serial**

```Bash
[root@https-ca ~]# openssl x509 -in /etc/pki/tls/cert.pem  -noout -serial -subject
serial=5EC3B7A6437FA4E0
subject= /CN=ACCVRAIZ1/OU=PKIACCV/O=ACCV/C=ES
```

2、吊销证书

先根据客户提交的serial与subject信息，对比检验是否与index.txt文件中的信息一致；然后

```Bash
[root@https-ca ~]# openssl ca -revoke /etc/pki/CA/newcerts/01.pem
```

3、生成吊销证书的编号

第一次吊销一个证书时才需要执行

```Bash
[root@https-ca ~]# echo 01 > /etc/pki/CA/crlnumber
```

4、更新证书吊销列表**

```Bash
[root@https-ca ~]# openssl ca -gencrl -out thisca.crl
```

5、查看证书吊销列表**

```Bash
[root@https-ca ~]# openssl crl -in /root/thisca.crl -noout -text
```

### 4、nginx HTTPS 部署实战

1. 申请证书与认证
2. 证书下载与配置
3. 问题分析与总结

#### 1、申请证书与认证

要搭建https服务首先需有SSL证书，证书通常是在第三方申请，在阿里云的安全服务中有SSL证书这一项，可以在里面申请免费的证书；

> 也可以在自己电脑中生成，虽然也能完成加密，但是浏览器是不认可的，因此最好还是去第三方申请

#### 1、证书申请

阿里云提供免费的证书，不需要人工审核，用来做测试是非常不错的选择，申请地址如下URL。

```Bash
https://www.aliyun.com/product/cas?spm=5176.10695662.958455.1.3f9140d5NlT5bZ
```

免费型的证书隐藏的比较深，想要申请免费证书需要先选择 1个域名->Symantec->免费型  ,所以读者这里需要注意一下

选择之后，一直点击下一步，便可购买完成，免费购买证书之后笔者需要回到证书控制台，在控制台有一个补全信息的链接地址，需要通过此地址补充申请人的联系信息

#### 2、域名验证

补全个人信息之后，还需要给阿里云验证当前域名是属于本人的，验证方式有两种，第一种是通过dns解析认证，第二种是通过上传验证文件认证，这里采用的是验证文件认证，首先需要下载文件

在下载验证文件完成之后，笔者需要把文件放到服务器中去，这里提供一条复制命令

```Bash
[root@web ~]#scp ~/Downloads/fileauth.txt  root@192.168.43.34:~/
```

将验证文件复制到服务器之后，还需要将验证文件放到站点对应目录，参考命令如下：

```Bash
[root@xiaoxuan ~]# cd /usr/share/nginx/html/
[root@xiaoxuan html]#mkdir -p /website/.well-known/pki-validation  &&  cp  fileauth.txt  /website/.well-known/pki-validation/
[root@xiaoxuan html]# cd && vim /etc/nginx/nginx.conf
server {
        listen       80;
        server_name  localhost;
        location / {
             root /usr/share/nginx/html/website;
        }
```

1、手动验证

手动验证的目的是首先确保文件位置放置是否正确，可以通过访问站点的url是否成功进行判断，比如笔者可以访问如下URL，如果返回如果页面能够正常打开，并且可以看到某些值，则代表配置成功。

```Bash
http://www.qf.com/.well-known/pki-validation/fileauth.txt
```

为干预，所以很快就能下发证书，下发证书的时间大约是2分钟左右。

#### 2、证书下载与配置

#### 1、证书下载

证书签发之后，可以在列表中可以看到状态栏中为 已签发 ，同时操作栏可以下载以及查看详情等

点击下载后，会跳转到下载详情页面，在下载详情页可以选择自己相对应的web服务，比如使用nginx，当选择nginx之后，下方还会很贴心的提示如何配置，下载nginx配置文件。

下载配置文件之后，需要将其解压，解压之后可以看见里面包含了两个证书文件

xxx.key

xxx.pem

接着需要把这两个证书文件给复制到服务器当中去，首先需要在服务器创建对应的文件夹，参考命令如下

```Bash
[root@xiaoxuan ~]# cd /etc/nginx/ && mkdir cert
```

在服务器创建完成对应文件夹之后，将证书文件复制到服务器中

```Bash
[root@xiaoxuan ~]# ls
2447549_www.testpm.cn_nginx.zip
[root@xiaoxuan ~]# unzip 2447549_www.testpm.cn_nginx.zip
Archive:  2447549_www.testpm.cn_nginx.zip
Aliyun Certificate Download
  inflating: 2447549_www.testpm.cn.pem  
  inflating: 2447549_www.testpm.cn.key   
[root@xiaoxuan ~]# ls
2447549_www.testpm.cn.key  2447549_www.testpm.cn_nginx.zip  2447549_www.testpm.cn.pem
[root@xiaoxuan ~]# cp 2447549_www.testpm.cn* /etc/nginx/cert/
[root@xiaoxuan ~]# cd /etc/nginx/cert/
[root@xiaoxuan cert]# mv 2447549_www.testpm.cn.key www.testpm.cn.key 
[root@xiaoxuan cert]# mv 2447549_www.testpm.cn.pem www.testpm.cn.pem
```

#### 2、证书配置

证书复制完成之后，可以对nginx配置文件进行更改，使用vim命令编辑nginx配置文件，参考命令如下：

```Bash
[root@xiaoxuan ~]# cd /etc/nginx/conf.d/
[root@xiaoxuan conf.d]# cp default.conf default.conf.bak
[root@xiaoxuan conf.d]# mv default.conf nginx_ssl.conf
[root@xiaoxuan conf.d]# vim nginx_ssl.conf
[root@xiaoxuan conf.d]# cat /etc/nginx/conf.d/nginx_ssl.conf 
server {
    listen 443 ssl;
    server_name www.testpm.cn;
    access_log  /var/log/nginx/https_access.log  main;

    #ssl on;
    ssl_certificate   /etc/nginx/cert/2447549_www.testpm.cn.pem;
    ssl_certificate_key  /etc/nginx/cert/2447549_www.testpm.cn.key;
    ssl_session_timeout 5m;
    ssl_protocols TLSv1 TLSv1.1 TLSv1.2;
    ssl_ciphers  ALL:!ADH:!EXPORT56:RC4+RSA:+HIGH:+MEDIUM:+LOW:+SSLv2:+EXP;
    ssl_prefer_server_ciphers on;

    location / {
        root  /usr/share/nginx/html;
        index index.html index.htm;
    }
}
```

#### 3、重启Nginx

修改配置文件之后，需要测试nginx配置文件是否正确

```Bash
[root@xiaoxuan cert]# nginx -t 
nginx: the configuration file /etc/nginx/nginx.conf syntax is ok
nginx: configuration file /etc/nginx/nginx.conf test is successful
[root@xiaoxuan cert]# nginx -s reload 
```

如果看到浏览器，展示安全，并且显示绿色就说明大功告成了!