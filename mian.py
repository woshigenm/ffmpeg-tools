import os
import re
import random
import calendar;
import time;
        
os.system("clear")
os.system("toilet -f mono12 -F gay 'Tools'")
def nm(number):
 try:
   if len(number)==0:
       return False
   else:
    if type(number)==type("nm"):
      return True
    else:
       return False
 except:
      return False 
      
def xnm(nux):
  try:
    if len(nux)==0:
      return False      
    else:
       if type(nux)==type(1) or type(nux)==type(1.1) or type(nux)==type(1+1j):
             return True
       else:
             return False
  except: 
       return False           
           
global num
print("""
0-查看支持格式        1-获取视频信息
2-下载m3u8            3-录制直播源
4-删除视频的音频      5-转换视频格式
6-视频压编码          7-提取视频音频
8-调整视频尺寸        9-光流法补帧
10-视频本体倒放       11-视频音频倒放
12-音频视频合体       13-PDF转格式
14-裁剪视频           15-转换视频比例
16-添加图像音频       17-时间剪视频文件
18-时间剪音频文件     19-切分视频
20-合并视频           21-添加字幕文件
22-转换字幕           23-视频倍率
24-图片合成视频       25-视频转GIF
26-照片合成视频       27-视频提音频
29-视频提截取片       30-照片合视频
31-提取音频           32-速率播放
33-画中画             35-添加水印
36-翻转               37-音频合并 
38-音频混音           39-补帧
40-调整音量           41-创空音频
43-截取缩微图         44-图片转换
45-图片转换           46-裁剪图片
47-旋转图片           48-图片黑白
49-图片加水印         49-修改比特率
51-翻转视频           52-高斯模糊
53-视频合音频         54-GIF转mp4
55-图片视频封面       56-退出""")
try:
   num =int(input('输入[0-67]:'))
   if num == 0:
    os.system('"clear"')
    print("请查看:")
    os.system('ffmpeg -formats')
    print("请输入正确的值")    
   if num == 1:
    os.system("clear")
    os.system("ls")
    o=str(input("视频文件:"))
    os.system('ffmpeg -i {}'.format(o))
    print("请输入正确的值")    
   if num == 2:
    os.system("clear")
    m=str(input("m3u8链接:"))
    if nm(m):
      p=str(input("视频保存名称(带路径,带后缀):"))
      if nm(p):
        os.system('ffmpeg -y -hide_banner -threads 16 -i {} -vcodec copy -acodec copy {}' .format(m,p))
      else:
       print("请输入正确的值")    
    else:
       print("请输入正确的值")
   if num == 3:
    os.system("clear")
    m=str(input("直播源"))
    if nm(m):
      p=str(input("视频保存名称(带后缀):"))
      if nm(p):
        os.system('ffmpeg -y -hide_banner -threads 16 -i {} -c copy {}'.format(m,p))
      else:
       print("请输入正确的值")      
    else:
       print("请输入正确的值")
   if num == 4:
    os.system("clear")
    os.system("ls")
    o=str(input("视频文件:"))
    if nm(o):
      t=str(input("保存地址:"))
      if nm(t):
        os.system('ffmpeg -y -hide_banner -threads 16 -i {} -an {}'.format(o,t))
      else:
       print("请输入正确的值")    
    else:
       print("请输入正确的值")
   if num == 5:
    os.system("clear")
    os.system("ls")
    o=str(input("视频文件:"))
    if nm(o):
      t=str(input("保存地址:"))
      if nm(t):
        os.system('ffmpeg -y -hide_banner -threads 16 -i {} -sameq {}'.format(o,t))
      else:
       print("请输入正确的值")      
    else:
       print("请输入正确的值")    
   if  num == 6:
    os.system("clear")
    os.system("ls")
    o=str(input("视频文件:"))
    if nm(o):
      g=str(input("压制编码(264或265):"))
      if xnm(g):
        print("Crf值越大,画质越差,文件越小(0-51):")
        crf =str(input("Crf值:"))
        if xnm(crf):
          t=str(input("保存地址:"))
          if nm(t):
            os.system('ffmpeg -y -hide_banner -threads 16 -i {} -c:v libx{} -crf {} -c:a copy {}'.format(o,g,crf,t))
          else:
            print("请输入正确的值")                     
        else:
          print("请输入正确的值")  
      else:
         print("请输入正确的值")      
    else:
        print("请输入正确的值")
   if  num == 7:
    os.system("clear")
    os.system("ls")
    o=str(input("视频文件:"))
    if nm(o):
      t=str(input("保存地址:"))
      if nm(t):
        os.system('ffmpeg -hide_banner -threads 16 -i {} -vn -c copy {}' .format(o,t))
      else:
         print("请输入正确的值")      
    else:
       print("请输入正确的值")    
   if  num == 8:
    os.system("clear")
    os.system("ls")
    o=str(input("视频文件:"))
    if nm(o):
      print("尺寸大小 ——如 1280:720")
      s=str(input("尺寸:"))
      if nm(s):
        t=str(input("保存地址:"))
        if nm(t):
          os.system('ffmpeg -hide_banner -threads 16 -i {} -filter:v scale=%s -c:a copy {}' .format(o,s,t))
        else:
           print("请输入正确的值")        
      else:
         print("请输入正确的值")      
    else:
       print("请输入正确的值")    
   if  num == 9:
    os.system("clear")
    print("请选择")
    os.system("ls")
    o=str(input("视频文件:"))
    if nm(o):
      e=str(input("帧数:"))
      if xnm(e):
        f=str(input("保存地址:"))
        if nm(f):
          os.system('ffmpeg -y -hide_banner -i {} -filter_complex "[0:v]scale=-2:-2[v];[v]minterpolate="mi_mode=mci:mc_mode=aobmc:me_mode=bidir:mb_size=16:vsbmc=1:fps={}"" -max_muxing_queue_size 1024  {} && am broadcast -a android.intent.action.MEDIA_SCANNER_SCAN_FILE  -d {}'.format(o,e,f,f))
        else:
          print("请输入正确的值")  
      else:
         print("请输入正确的值")      
    else:
       print("请输入正确的值")    
   if  num == 10:
    os.system("clear")
    os.system("ls")
    o=str(input("视频文件:"))
    if nm(o):
      t=str(input("保存地址:"))
      if nm(t):      
        os.system('ffmpeg -y -hide_banner -threads 16 -i {} -vf reverse -af areverse  {} && am broadcast -a android.intent.action.MEDIA_SCANNER_SCAN_FILE  -d {}'.format(o,t,t))
      else:
       print("请输入正确的值")      
    else:
       print("请输入正确的值")    
   if  num == 11:
    os.system("clear")
    os.system("ls")
    o=str(input("视频文件:"))
    if nm(o):
      t=str(input("保存地址:"))
      if nm(t):
        os.system('ffmpeg -y -hide_banner -threads 16 -i {} -af areverse  {} && am broadcast -a android.intent.action.MEDIA_SCANNER_SCAN_FILE  -d {}'.format(o, t, t))
      else:
       print("请输入正确的值")      
    else:
       print("请输入正确的值")
   if  num ==13:
    os.system("clear")
    os.system("ls")
    e=str(input("PDF文件(不带后缀):"))
    if nm(e):
      o=str(input("图片密度:"))
      if nm(o):
        t=str(input("图片名:"))
        if nm(t):        
          f=str(input("图片格式:"))
          if nm(f):            
           os.system('convert -density {} {}.pdf {}.{}'.format(o,e,t,f))
          else:
            print("请输入正确的值")                      
        else:
           print("请输入正确的值")        
      else:
        print("请输入正确的值")      
    else:
       print("请输入正确的值")        
   if  num == 14:
    os.system("clear")
    os.system("ls")
    o=str(input("视频:"))
    if nm(o):
      e=str(input("裁剪宽度:"))
      if xnm(e):      
        f=str(input("裁剪高度:"))
        if xnm(f):
          five=str(input("x轴裁剪位:"))
          if xnm(five):
            six=str(input("y轴裁剪位:"))
            if xnm(six):
              t=str(input("保存地址:"))
              if nm(t):
                os.system('ffmpeg -y -hide_banner -threads 16 -i {} -filter:v "crop={}:{}:{}:{}" {}'.format(o,e,f,five,six,t))
              else:
               print("请输入正确的值")                        
            else:
              print("请输入正确的值")                          
          else:
             print("请输入正确的值")                       
        else:
           print("请输入正确的值")        
      else:
         print("请输入正确的值")       
    else: 
       print("请输入正确的值")
   if  num == 15:
    os.system("clear")
    o=str(input("视频(后缀):"))
    if nm(o):
       e=str(input("保存地址"))
       if nm(e):
          t=str(input("比例(16:9):"))
          if nm(t):
            os.system('ffmpeg -y -hide_banner -threads 16 -i {} -aspect {} {}'.format(o,t,e))
          else:
            print("请输入正确的值")                      
       else:
         print("请输入正确的值")       
    else:
      print("请输入正确的值")      
   if  num == 16:
    os.system("clear")
    os.system("ls")
    o=str(input("视频:"))
    if nm(o):
       t=str(input("插入的图片:"))
       if nm(t):
         e=str(input("保存地址"))
         if nm(e):
           os.system('ffmpeg -y -hide_banner -threads 16 -loop 1 -i {} -i {} -c:v libx264 -tune stillimage -c:a aac -b:a 192k -shortest {}'.format(o,t,e))
         else:
           print("请输入正确的值")         
       else:
          print("请输入正确的值") 
    else:
       print("请输入正确的值")
   if  num == 17:
    os.system("clear")
    os.system("ls")
    o=str(input("视频:"))
    if nm(o):
       t=str(input("开始时间:"))
       if xnm(t):
          e=str(input("截取时间(秒):"))
          if xnm(e):
            print("如果不想改变视频的bit率,两个参数可以不填") 
            l=str(input("是否输入bit格式(-b:v)"))
            h=str(input("bit率:"))
            f=str(input("保存地址:"))
            if nm(f):
              os.system('ffmpeg -y -hide_banner -threads 16 -ss {} -t {} -i {} -codec copy -keyint_min 2 -g 1 {} {} {}'.format(t,e,o,l,h,f))
            else:
              print("请输入正确的值")                         
          else:
            print("请输入正确的值")
       else:
          print("请输入正确的值")  
    else:
       print("请输入正确的值")
   if  num == 18:
    os.system("clear")
    os.system("ls")
    o=str(input("音频:"))
    if nm(o):
      t=str(input("开始时间):"))
      if xnm(t):
        e=str(input("结束时间:"))
        if xnm(e):
          f=str(input("保存地址:"))
          if nm(f):
            os.system('ffmpeg -y -hide_banner -threads 16 -i {} -ss {} -to {} -c copy {}'.format(o,t,e,f))
          else:
            print("请输入正确的值")                      
        else:
           print("请输入正确的值")        
      else:
         print("请输入正确的值")      
    else:
        print("请输入正确的值")
   if  num == 19:
    os.system("clear")
    os.system("ls")
    o=str(input("音频:"))
    if nm(o):
       t=str(input("开始时间):"))
       if xnm(o):
          e=str(input("第一段视频保存地址:"))
          if nm(e):
             f=str(input("第二段视频保存地址:"))
             if nm(f):
               os.system('ffmpeg -y -hide_banner -threads 16 -i {} -t {} -c copy {} -ss {} -codec copy {}'.format(o,t,e,t,f))
             else:
               print("请输入正确的值")                       
          else:
           print("请输入正确的值")        
       else:
         print("请输入正确的值")       
    else:
      print("请输入正确的值")         
   if  num== 20:
    os.system("clear")
    os.system("ls")
    o=str(input("txt文件):"))
    if nm(o):
       t=str(input("保存地址:"))
       if nm(t):
         os.system('ffmpeg -y -hide_banner -threads 16 -f concat -safe 0 -i {}.txt -c copy {}'.format(o,t))
       else:
         print("请输入正确的值")      
    else:
        print("请输入正确的值")
   if  num == 21:
    os.system("clear")
    os.system("ls")
    o=str(input("音频:"))
    if nm(o):
      t=str(input("字幕文件(ass/srt/vtt):"))
      if nm(t):
        e=str(input("保存地址:"))
        if nm(e):
          os.system('ffmpeg -y -hide_banner -threads 16 -i {} -i {} -map 0 -map 1 -c copy -c:v libx264 -crf 23 -preset medium {}'.format(o,t,e))
        else:
          print("请输入正确的值")  
      else:
         print("请输入正确的值")      
    else:
       print("请输入正确的值")    
   if  num == 22:
    os.system("clear")
    os.system("ls")
    o=str(input("字幕文件:"))
    if nm(o):
       t=str(input("转化格式:"))
       if nm(t):
         os.system('ffmpeg -y -hide_banner -threads 16 -i {} {}'.format(o,t))
       else:
        print("请输入正确的值")      
    else:
       print("请输入正确的值")
   if  num == 23:
    os.system("clear")
    os.sysytem("ls")
    o=str(input("视频:"))
    if nm(o):
      print("注意:加快视频的速度,不会加快音频速度")
      t=str(input("倍速:"))
      if xnm(t):
        e=str(input("保存地址:"))
        if nm(e):
           os.system('ffmpeg -y -hide_banner -threads 16 -i {} -vf "setpts={}*PTS" {}'.format(o,t,e))
        else:
          print("请输入正确的值")
      else:
        print("请输入正确的值")     
    else:
       print("请输入正确的值")    
   if  num == 24:
    os.system("clear")
    os.system("ls")
    o=str(input("多张图片目录:"))
    if nm(o):
      f=str(input("帧率:"))
      if xnm(f):
        print("格式请为"+"图片名01.jpg")
        t=str(input("图片格式:"))
        if nm(t):
          e=str(input("视频保存地址:"))
          if nm(e):
            os.system('ffmpeg -y -hide_banner -threads 16 -framerate {} -i {}%01d{} -c:v libx264 -r 30 -pix_fmt yuv420p {}'.format(f,o,t,e))
          else:
             print("请输入正确的值")                   
        else:
          print("请输入正确的值")  
      else:
         print("请输入正确的值")
    else:
       print("请输入正确的值")    
   if  num == 25:
    os.system("clear")
    os.system("ls")
    t=str(input("视频:"))
    if nm(t):
       o=str(input("截取时间:"))
       if xnm(o):
         e=str(input("视频地址(不带后缀):"))
         if nm(e):
           os.system('ffmpeg -y -hide_banner -threads 16 -ss {} -i {} -to 10 -r 10 -vf scale=200:-1 {}.gif'.format(o,t,e))
         else:
           print("请输入正确的值")         
       else:
          print("请输入正确的值") 
    else:
        print("请输入正确的值")
   if  num == 26:
    os.system("clear")
    os.system("ls")
    o=str(input("图片名(不用后缀):"))
    if nm(o):
      t=str(input("图片格式:"))
      if nm(t):
         s=str(input("帧率:"))
         if xnm(s):
           six=str(input("音频:"))
           if nm(t):
             e=str(input("合成的视频格式:"))
             if nm(e):
                os.system('ffmpeg -y -hide_banner -threads 16 -y -r {} -i {}%d.{} -i {} -absf aac_adtstoasc {}'.format(s,o,t,six,e))
             else:
              print("请输入正确的值")                      
           else:
             print("请输入正确的值")                 
         else:
            print("请输入正确的值")             
      else:
         print("请输入正确的值")      
    else:
       print("请输入正确的值")    
   if  num == 27:
    os.system("clear")
    os.system("ls")
    o=str(input("视频:"))
    if nm(o):
       t=str(input("音频保存地址:"))
       if nm(t):
         os.system('ffmpeg -y -hide_banner -threads 16 -i {} -vn {}'.format(o,t))
       else:
          print("请输入正确的值")            
    else:
       print("请输入正确的值")    
   if  num == 29:
    os.system("clear")
    os.system("ls")
    o=str(input("视频:"))
    if nm(o):
       f=str(input("帧率:"))
       if xnm(f):
         t=str(input("图片名:"))
         if nm(t):
           e=str(input("图片格式:"))
           if nm(e):
             os.system('ffmpeg -y -hide_banner -threads 16 -i {} -r {} -f image2 {}%1d.{}'.format(o,f,t,e))
           else:
              print("请输入正确的值")                   
         else:
           print("请输入正确的值")   
       else:
         print("请输入正确的值")   
    else:
       print("请输入正确的值")    
   if  num ==30:
    os.system("clear")
    os.system("ls")
    o=str(input("照片(不带后缀):"))
    if nm(o):
      t=str(input("格式:"))
      if nm(t):
        e=str(input("帧率:"))
        if nm(e):
          ten=str(input("码率:"))
          if nm(ten):
            f=str(input("输出视频地址:"))
            if nm(f):
              os.system('ffmpeg -y -hide_banner -threads 16 -r {} -i "{}%1d.{}" -vcodec mpeg4 -b:v {}k {}'.format(e,o,t,ten,f))
            else:
               print("请输入正确的值")                   
          else:
            print("请输入正确的值")                 
        else:
          print("请输入正确的值")             
      else:
         print("请输入正确的值")  
    else:
       print("请输入正确的值")
   if  num ==12:
    os.system("clear")
    os.system("ls")
    o=str(input("视频:"))
    if nm(o):
       t=str(input("音频:"))
       if nm(t):
         e=str(input("保存地址:"))
         if nm(e):
           os.system('ffmpeg -y -hide_banner -threads 16 -i {} -i {} -vcodec copy -acodec copy {}'.format(o,t,e))
         else:
            print("请输入正确的值")               
       else:
          print("请输入正确的值")            
    else:
       print("请输入正确的值")
   if  num == 31:
    os.system("clear")
    os.system("ls")
    o=str(input("视频:"))
    if nm(o):
      t=str(input("音频保存地址:"))
      if nm(t):
        e=str(input("音频格式:"))
        if nm(e):
          os.system('ffmpeg -y -hide_banner -threads 16 -i {} -acodec copy -vn {}.{}'.format(o,t,e))
        else:
           print("请输入正确的值")    
      else:
         print("请输入正确的值")   
    else:
       print("请输入正确的值")    
   if  num == 32:
    os.system("clear")
    os.system("ls")
    o=str(input("视频:"))
    if nm(o):
       t=str(input("速率:"))
       if nm(t):
          e=str(input("保存地址:"))
          if nm(e):
            os.system('ffmpeg -y -hide_banner -threads 16 -i {} -filter_complex "[0:v]setpts={}*PTS[v];[0:a]atempo=2.0[a]" -map "[v]" -map "[a]" {}'.format(o,t,e))
          else:
            print("请输入正确的值")            
       else:
         print("请输入正确的值")
    else:
       print("请输入正确的值")    
   if  num == 33:
    os.system("clear")
    os.system("ls")
    o=str(input("主视频:"))
    if nm(o):
      t=str(input("画中画视频:"))
      if nm(t):
        e=str(input("宽:"))
        if xnm(e):
          f=str(input("高:"))
          if xnm(f):
            five=str(input("宽:"))
            if xnm(five):
              ten=str(input("高:"))
              if xnm(ten):
                six=str(input("保存地址:"))
                if nm(six):
                  os.system('ffmpeg -y -hide_banner -threads 16 -i {} -i {} -filter_complex "[1:v]scale=w={}:h={}:force_original_aspect_ratio=decrease[ckout];[0:v][ckout]overlay=x=W-w-{}:y={}[out]" -map "[out]" -movflags faststart {}'.format(o,t,e,f,five,ten,six))
                else:
                  print("请输入正确的值")                       
              else:
                print("请输入正确的值")                     
            else:
               print("请输入正确的值")                   
          else:
            print("请输入正确的值")                 
        else:
           print("请输入正确的值")   
      else:
         print("请输入正确的值")
    else:
       print("请输入正确的值")
   if  num == 34:
    os.system("clear")
    os.system("ls")
    o=str(input("视频:"))
    if xnm(o):
      mao=str(input("秒:"))
      if nm(mao):
        t=str(input("水印图片:"))
        if nm(t):
           e=str(input("宽(宽:高):"))
           if nm(e):
             f=str(input("高(宽:高):"))
             if nm(f):
               five=str(input("视频保存地址:"))
               if nm(five):
                 os.system('ffmpeg -y -hide_banner -threads 16 -i {} -itsoffset {} -filter_complex "movie={},scale={}[w];[0:v]curves=vintage[o];[o][w]overlay={} [out]" -map "[out]" -map 0:a {}'.format(o,mao,t,e,f,five))
               else:
                print("请输入正确的值")                          
             else:
                print("请输入正确的值")                    
           else:
              print("请输入正确的值")              
        else:
          print("请输入正确的值")         
      else:
        print("请输入正确的值")
    else:
       print("请输入正确的值")
   if  num ==35:
    os.system("clear")
    print("也可以视频哦凸( •̀_•́ )凸")
    os.system("ls")
    o=str(input("图片:"))
    if nm(o):
      t=str(input("翻转样式(hflip,vflip,rotate,transpose):"))
      if nm(t):
        e=str(input("保存地址:"))
        if nm(e):
          os.system('ffmpeg -y -hide_banner -threads 16 -i {} -vf {} -y {}'.format(o,t,e))
        else:
          print("请输入正确的值")          
      else:
         print("请输入正确的值")
    else:
       print("请输入正确的值")
   if  num == 36:
    os.system("clear")
    os.system("ls")
    o=str(input("音频:"))
    if nm(o):
       t=str(input("音频:"))
       if nm(t):
         e=str(input("保存地址:"))
         if nm(e):
           nm=' -map [a] {}'.format(e)
           cnm="'[0:0] [1:0] concat=n=2:v=0:a=1 [a]'"
           c='ffmpeg -y -hide_banner -threads 16 -i {} -i {} -filter_complex'.format(o,t)
           os.system(c+cnm+nm)
         else:
           print("请输入正确的值")
       else:
         print("请输入正确的值")
    else:
       print("请输入正确的值")
   if  num ==37:
    os.system("clear")
    os.system("ls")
    o=str(input("音频:"))
    if nm(o):
      t=str(input("音频:"))
      if nm(t):
        e=str(input("保存地址:"))
        if nm(e):
           os.system('ffmpeg -y -hide_banner -threads 16-i {} -i {} -filter_complex "[0:a] [1:a]amerge=inputs=2[aout]" -map "[aout]" -ac 2 {}'.format(o,t,e))
        else:
          print("请输入正确的值")          
      else:
        print("请输入正确的值")
    else:
       print("请输入正确的值")
   if  num ==38:
    os.system("clear")
    os.system("ls")
    o=str(input("视频:"))
    if nm(o):
      t=str(input("保存地址:"))
      if nm(t):
        os.system('ffmpeg -y -hide_banner -threads 16 -i {} -filter_complex "minterpolate=fps=60" {}'.format(o,t))
      else:
         print("请输入正确的值")
    else:
       print("请输入正确的值")    
   if  num == 39:
    os.system("clear")
    os.system("ls")
    o=str(input("视频文件:"))
    if nm(o):
       t=str(input("大小(数字):"))
       if xnm(t):
         e=str(input("视频文件保存地:"))
         if nm(e):
           c='ffmpeg -y -hide_banner -threads 16 -i {} -af "volume={}" {}'.format(o,t,e)
           os.system(c)
         else:
            print("请输入正确的值")            
       else:
          print("请输入正确的值")          
    else:
       print("请输入正确的值")
   if  num == 41:
    os.system("clear")
    o=str(input("音频保存地址"))
    if nm(o):
      os.system('ffmpeg -y -hide_banner -threads 16-f lavfi -i anullsrc -t 20 {}'.format(o))
    else:
       print("请输入正确的值")
   if  num == 43:
    os.system("clear")
    os.system("ls")
    o=str(input("视频:"))
    if nm(o):
      t=str(input("截取时间(秒):"))
      if xnm(t):
        e=str(input("截取图片长:"))
        if xnm(e):
          h=str(input("截取图片长宽:"))
          if xnm(h):           
            f=str(input("保存地址:"))
            if nm(f):           
              os.system('ffmpeg -y -hide_banner -threads 16 -i {} -y -f image2 -ss {} -t 0.001 -s {}×{} t {}'.format(o,t,e,h,f))
            else:
               print("请输入正确的值")               
          else:
             print("请输入正确的值")             
        else:
            print("请输入正确的值")            
      else:
         print("请输入正确的值")
    else:
       print("请输入正确的值")
   if  num == 44:
    os.system("clear")
    os.system("ls")
    o=str(input("照片:"))
    if nm(o):
      size=str(input("大小"))
      if xnm(size):
        t=str(input("保存文件名:"))
        if nm(t):
          os.system('convert -sample {} {} {}'.format(size,o,t))
        else:
           print("请输入正确的值")
      else:
        print("请输入正确的值")
   if  num == 45:
    os.system("clear")
    os.system("ls")
    t=str(input("图片:"))
    if nm(t):     
      o=str(input("截取长:"))
      if xnm(o):
        nm=str(input("图片宽:"))
        if xnm(nm):
          e=str(input("图片保存地址:"))
          if nm(e):
            os.system('convert -resize {}x{} {} {}'.format(o,nm,t,e))
          else:
            print("请输入正确的值")            
        else:
           print("请输入正确的值")
      else:
         print("请输入正确的值")
    else:
       print("请输入正确的值")
   if  num == 46:
    os.system("clear")
    os.system("ls")
    five=str(input("图片:"))
    if nm(five):    
      o=str(input("图片长:"))
      if xnm(o):
        t=str(input("图片宽:"))
        if xnm(t):
          e=str(input("裁剪图片的x轴:"))
          if xnm(e):          
            f=str(input("裁剪图片的y轴):"))
            if xnm(f):
              six=str(input("保存地址:"))
              if nm(six):
                os.system('convert -crop {}x{}+{}+{} {} {}'.format(o,t,e,f,five,six))
              else:
                 print("请输入正确的值")                 
            else:
              print("请输入正确的值")              
          else:
             print("请输入正确的值")             
        else:
           print("请输入正确的值")
      else:
        print("请输入正确的值")
    else:
       print("请输入正确的值")
   if  num == 47:
    os.system("clear")
    os.system("ls")
    t=str(input("图片):"))
    if nm(t):
      o=str(input("度数(顺时针):"))
      if xnm(o):       
        e=str(input("保存地址:"))
        if nm(e):
          os.system('convert -rotate {} {} {}'.format(o,t,e))
        else:
           print("请输入正确的值")
      else:
         print("请输入正确的值")
    else:
       print("请输入正确的值")
   if  num == 48:
    os.system("clear")
    os.system("ls")
    o=str(input("图片:"))
    if nm(o):      
      t=str(input("保存地址:"))
      if nm(t):
         os.system('convert -monochrome {} {}'.format(o,t,))
      else:
         print("请输入正确的值")    
    else:
       print("请输入正确的值")   
   if  num == 49:
    os.system("clear")
    os.system("ls")
    o=str(input("图片:"))
    if nn(o):
      t=str(input("水印图:"))
      if nm(t):     
        e=str(input("下边距:"))
        if xnm(e):
          f=str(input("右边距:"))
          if xnm(f):
            five=str(input("保存地址:"))
            if nm(five):
              os.system('convert {} {} -gravity southeast -geometry +{}+{} -composite {}'.format(o,t,e,f,five))
            else:
              print("请输入正确的值")              
          else:
             print("请输入正确的值")           
        else:
           print("请输入正确的值") 
      else:
         print("请输入正确的值")
    else:
       print("请输入正确的值")    
   if  num== 50:
    os.system("clear")
    os.system("ls")
    o=str(input("文件地址"))
    if nm(o):
      print("音频-b:a 视频:-b:v")
      t=str(input("请选择:"))
      p=str(input("bit率大小(100k):"))
      e=str(input("保存地址:"))
      if nm(e):      
         os.system('ffmpeg -y -hide_banner -threads 16 -i {} {} {} {}'.format(o,t,p,e))
      else:
        print("请输入正确的值")
    else:
       print("请输入正确的值")
   if  num==51:
    os.system("clear")
    os.system("ls")
    o=str(input("视频文件:"))
    if nm(o):
      t=str(input("翻转角度:"))
      if nm(t):
        w=str(input("保存地址:"))
        if nm(w):
          os.system('ffmpeg -y -hide_banner -threads 16 -i {} -metadata:s:v rotate="{}" -codec copy {}'.format(o,t,w))
        else:
           print("请输入正确的值")
      else:
         print("请输入正确的值")
    else:
       print("请输入正确的值")
   if  num==52:
    os.system("clear")
    os.system("ls")
    o=str(input("视频文件:"))
    if nm(o):
      m=str(input("保存地址:"))
      if nm(m):
        os.system('ffmpeg -y -hide_banner -threads 16 -i {} -vf gblur=sigma=0.6:steps=1 {}'.format(o,m))
      else:
       print("请输入正确的值")
    else:
       print("请输入正确的值")
   if num==53:
     os.system("clear")
     os.system("ls")
     one=str(input("视频文件:"))
     if nm(one):
       two=str(input("音频文件:"))
       if nm(two):
         three=str(input("保存地址:"))
         if nm(three):       
           os.system('ffmpeg -hide_banner -i {} -i {} -y {}'.format(one,two,three))
         else:
            print("请输入正确的值")            
       else:
          print("请输入正确的值")          
     else:
        print("请输入正确的值")
   if num==54:
     os.system("clear")
     os.system("ls")
     one=str(input("GIF文件:"))
     if nm(one):
      two=str(input("保存地址(不带后缀):"))
      if nm(two):
         os.system('ffmpeg -y -hide_banner -f gif -i {} {}.flv'.format(one,two))
         os.system('ffmpeg -y -hide_banner -i {}.flv {}.mp4'.format(two,two))
         os.system('rm {}.flv'.format(two))
      else:
         print("请输入正确的值")
     else:
         print("请输入正确的值")
   if num ==55:
    os.system("clear")
    os.system("ls")
    one=str(input("视频文件:"))
    if nm(one):
      two=str(input("图片:"))
      if nm(two):
        three=str(input("保存地址: "))
        if nm(three):          
          os.system('ffmpeg -y -hide_banner -i {} -i {} -map 0 -map 1 -c copy -c:v:1 png -disposition:v:1 attached_pic {}'.format(one,two,three))
        else:
           print("请输入正确的值")
      else:
         print("请输入正确的值")
    else:
        print("请输入正确的值")
   if num ==56:
     print("程序已退出")
     exit()
except:
      print("请输入正确的值")
