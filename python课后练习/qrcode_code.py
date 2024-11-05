# import qrcode

# qr = qrcode.QRCode(
#     version=1,
#     error_correction=qrcode.constants.ERROR_CORRECT_L,
#     box_size=10,
#     border=4,
# )
# qr.add_data('www.baidu.com')
# qr.make(fit=True)

# img = qr.make_image(fill_color="black", back_color="white")

# img.save('qrcode_code.png')



# ########################################################################################
import qrcode
from PIL import Image

# 创建一个带有中心图标的QR码
qr = qrcode.QRCode(
    error_correction=qrcode.constants.ERROR_CORRECT_H
)
qr.add_data('https://www.example.com')
qr.make()

# 生成QR码图像
img = qr.make_image(fill_color="black", back_color="white").convert('RGB')

# 加载logo图像并插入到QR码中心
logo = Image.open('qrcode_code.png')
logo.thumbnail((50, 50))
logo_pos = ((img.size[0] - logo.size[0]) // 2, (img.size[1] - logo.size[1]) // 2)
img.paste(logo, logo_pos)

# 保存生成的QR码
img.save('custom_qr.png')

##############################################################################




import qrcode

# 生成WiFi访问信息的QR码
ssid = "ExampleNetwork"
password = "securepassword123"
wifi_info = f"WIFI:T:WPA;S:{ssid};P:{password};;"
wifi_qr = qrcode.make(wifi_info)
wifi_qr.save('wifi_qr.png')

##############################################################################