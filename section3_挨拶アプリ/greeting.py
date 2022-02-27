import tkinter
from PIL import ImageTk, Image

#ウィンドウの作成
root = tkinter.Tk()
root.title('あいさつアプリ') #タイトル
root.iconbitmap("./icon/greeting.ico") #アイコン画像　#https://icon-icons.com/ja/ #https://icons8.jp/
root.geometry('400x400') #サイズ #横x縦
root.resizable(0,0) #サイズの変更を許可するかどうか #0:許可しない、1:許可する

#色の定義
output_color = '#A9A9A9'

#フレームの作成
input_frame = tkinter.Frame(root) #rootウィンドウにフレームを作る
output_frame = tkinter.LabelFrame(root, bg=output_color) #bg:背景色 #https://ironodata.info/search/
input_frame.pack(pady=10)
output_frame.pack(fill='both', expand=True) #fill='both':横縦共に引き延ばされた状態になる #expand=True:縦方向にも引き延ばしたい場合

#ボタン画像の読み込み
submit_img = tkinter.PhotoImage(file='./icon/submit.png')
# submit_img = ImageTk.PhotoImage(Image.open('./icon/submit.png')) #JPGの場合はこちらの方法でのみ可

#エントリー&ボタンの作成
name = tkinter.Entry(input_frame, width=30)
name.insert(0, '名前を入力してください')
submit_button = tkinter.Button(input_frame, image=submit_img)
name.grid(row=0, column=0, padx=10, pady=10)
submit_button.grid(row=0, column=1, padx=10, pady=10)

#ウィンドウのループ処理
root.mainloop()
