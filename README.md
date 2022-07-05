<h1 align="center">Serein | rain falling from a cloudless sky</h1>  
<p align="center"><img src="https://socialify.git.ci/W01fh4cker/Serein_Linux/image?description=1&descriptionEditable=A%20tool%20for%20graphically%20collecting%20URLs%20in%20batches%2C%20and%20performing%20various%20nday%20detections%20on%20the%20collected%20URLs%20in%20batches.%20&font=Bitter&forks=1&issues=1&language=1&logo=https%3A%2F%2Fs2.loli.net%2F2022%2F06%2F25%2FgUAh2V5CiD96y8G.jpg&owner=1&pulls=1&stargazers=1" /></p>

# Declaration

1. This project is only for authorized use. It is prohibited to use this project for illegal operations, otherwise you will be responsible for the consequences. Please abide by the laws of your country! ! !
2. I wrote it after staying up late for a short period of time, and my head is dizzy. I expect there will be many mistakes. Please point out that my contact information has been posted below, I would be very grateful!
3. **Planning to add an exploit module every day in July, so welcome `star/fork`, every `star` and `fork` of yours is my motivation! **
# Latest-Interface-Display 
![0](https://s2.loli.net/2022/07/05/lt6GIZOyJnNKjHr.png)

# Exploit-Example

1. We want to exploit the `Fumeng Cloud AjaxMethod.ashx SQL injection` vulnerability in batches, so we `base64` encrypt the statement and get: `dGl0bGU9IuWtmuebn+S6kSAi`.

2. We choose to get the first `2000` (the specific number needs to be filled in according to your own membership):

   ![0](https://s2.loli.net/2022/07/05/jN8rJw6yzfbaUCM.png)

   ![1](https://s2.loli.net/2022/07/05/cZ2MgLXb1FoEUij.png)

   ![2](https://s2.loli.net/2022/07/05/xsQ9dCcPgmDaAoi.png)

3. Click directly on `Fumeng Cloud AjaxMethod.ashx SQLinjection [auto-muti-exp]`:

      ![3](https://s2.loli.net/2022/07/05/cRfwIa7QjYDpPCl.png)

4. You can see that the software starts batch testing：

      ![5](https://s2.loli.net/2022/07/05/iIG9a5L8bJVXvky.png)

5. **Delete the three files `urls.txt`, `corrected url.txt`, `host.txt` in the folder, and prepare to use other modules.**

# How-To-Use

1. ```python
   git clone https://github.com/W01fh4cker/Serein_Linux.git
   cd Serein_Linux
   pip3 install -r requirements.txt
   python3 Serein_Linux.py
   ```
   
2. Click `Software Configuration` in the upper left corner to configure `email` and `key` of `fofa` (note that it is not a password, but `API KEY` in `https://fofa.info/personalData`), then you can be happy to use `fofa search` instead.
    **Note: It must be a `fofa` ordinary/advanced/enterprise account, because `fofa` registered members need to consume `f` coins to call `api`, if you are a registered member, please make sure you have `f` coins, otherwise you cannot query ! **
4. After the collection is completed, `urls.txt`, `corrected url.txt`, `host.txt` will be generated in the same level directory of the software, and the `collected original url` , `url with http/https header added` and `Website IP only` will be saved respectively. 
5. After completing a scan task, to start the next scan, please delete the three files `urls.txt`, `correcturl.txt`, and `host.txt` in the folder.
6. If you encounter any problems in use and have lively ideas, you have three ways to communicate with me:

```python
mailto:sharecat2022@gmail.com

https://github.com/W01fh4cker/Serein/issues

Wechat: W01fh4cker
```


# To-Do List
1. Improve the weight query module. When we want to submit the vulnerability platform after one-click stud, because the platform has weight requirements, we need to carry out `ip-->domain` for the website containing the vulnerability, then reverse the domain name, and use multiple query interfaces for weighting Query, filter out websites that meet the weight requirements, and export them.
2. (Preferred) Add other search engines, such as: `Censys`, `Zoomeye`, `Quake`, etc.
3. Add proxy mode.
4. Others have not been thought of yet. If you have any ideas, you can put them directly in `issues`.

# W01fh4cker's interest exchange community
- `https://discord.gg/n2c5Eaw4Jx`

![image](https://user-images.githubusercontent.com/101872898/173513465-5c43767a-5dcd-4aa5-83ee-d7ea5c757bbb.png)  
# Star Growth Curve
[![Stargazers over time](https://starchart.cc/W01fh4cker/Serein.svg)](https://starchart.cc/W01fh4cker/Serein)
