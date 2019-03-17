# essential c++

1. ## 如何撰写c++程序 

   ###  代码块，　封装（命名空间）

2. ## 对象的定义与初始化　

   ### 对象命名要有意义，对象名称不能以数字开头

   ### 对象的初始化

   `int num(0) `（构造函数语法）　　`int num = 0`(沿袭自ｃ语言)

   如果对象需要多个初值，那么只能使｀构造函数语法的形式进行初始化｀比如｀

   `# include <complex>`

   `complex <double> purel (0,7)`

   对于`char`类型，有一些转义字符比如`\n`，其中`\`表示转义，可以搭配不同的符号

   被定义为`const`的对象，在获得初值之后无法再有任何变动

   ３．　撰写表达式

   `? :`表达式

   运算符优先级 

   # Effective C++

   ## 1. 让自己习惯c++

   ### １．C++为一个语言联邦

   Ｃ++包括C的语法，同时加入了OO的思想(C　with class) ,也加入了泛型编程的部分，同时还有STL库，学会合理运用

   ### ２．尽量用const, enum, inline 替换掉# define 

   宏会出现一些你想象不到的问题

   ### ３. 尽可能使用const   （不是很理解）                                                                                                                                                                                                                                                                                                                                                                                

   ```c++
   char greet [] = "hello";
   char* p = greet;			//nonconst pointer,nonconst data
   const char* p = greet;		//nonconst pointer,const data
   char* const p = greet;		//const pointer, nonconst data;
   char const * p=greet;		//const pointer, nonconst dat;
   const char* const p = greet;//const pointer,constdata
   ```

   编译器强制实施bitwise constness,　但是编写程序时应使用“概念上的常量性(conceptional constness)”

   当const和non-const成员函数有实质等价的实现时，令non-const 版本调用const版本可以避免代码重复

   ### ４．确定对象被使用前已经被初始化过

    对象未初始化会导致程序的不确定行为

   赋值和初始化不同概念

   ```c++
   class 	ABC{ ... };
   class AB{
       public:
       	AB(const std::dtring& name, const std::list<ABC> & phone);
       private:
       	std::string name;
       	std::list<ABC>thePhone;
       //赋值
       AB(const std::string& name, const std::list<ABC> & phone);
       {
               theName=name;
               thePhone=phone;
       }
       //采用成员初值列替换复制动作
       AB(const std::string & name,const std::list<ABC> & phone)
           :theName(name),
       	 thePhone(phone) {}
   }
   //二者的结果一样，但是下面的效率会比较高，赋值版本会调用default构造函数再赋予新值
   //后者会直接调用copy构造函数
   ```

   最好在初值列中列出所有成员变量，并给予初值，以免遗忘

   如果成员函数是const 或者reference,　它们一定需要初值，但是不能被赋值

   初始化次序按照先基类后派生类以及函数声明次序进行

   不同编译单元内定义之non-local static 对象的初始化次序？？？解决办法是用local static对象替换掉non-local对象

   ## 2. 构造/析构/赋值运算

   ### ５．了解C++默默编写并调用了那些函数

   每个类都会有一或多个构造函数，一个析构函数，一个拷贝构造函数，还有一个copy assignment 操作符

   ```c++
   class A
   {
       public:
       	A() { ... }							//构造函数（默认）
       	A(const A& rhs) { ... }				//拷贝构造函数
       	~A() { ... }						//析构函数
       
       	A& operator=(const A& rhs) { ... }  //=赋值运算符
   };
   ```

   编译器会为每个类创建一个默认的构造函数，一个默认的拷贝构造函数，和一个默认析构函数还有一个copy assignment 操作符

   ### ６．如果不想使用编译器自动生成的函数，应该明确的拒绝

   所有编译器产出的函数都是public，如果不希望某个函数被创造，例如不想类支持copy assignment操作符或者拷贝构造函数，那么可以把这些函数声明为private来阻止用户调用（这种处理办法不是很安全，因为友元函数和成员函数依然会调用）

   另外一个方法和上述方法是一样的，但是不是在自身这个类中操作，定义一个基类，在基类中将你不想要类执行的操作定义为private，然后使用继承关系

   ```c++
   class Uncopyable{
       protected:
       	Uncopyable() {}									//允许派生对象构造和析构
       	~Uncopyable() {}
       private:
       	Uncopyable(const Uncopyable& a) {}			 	//但是阻止copying
       	Uncopyeable& operator=(const Uncopyable& a) {} 	//
   };
   class HomeForSale:private Uncopyable{  //class 不再声明copy构造函数或者copy assignment									   //操作符
       ...
   };
   ```

### 7.为多态基类声明virtual析构函数

f<u>actory函数</u>

定义一个函数，“返回一个base class指针，指向新生成的derived class 对象“，这种情况时有发生，而且由于函数的特殊性，这类函数返回的对象必须位于heap，　因此必须在合适的时候将通过这种方式产生的对象删除掉，避免内存泄漏或者其他资源的泄露。但是在delete　对象的时候是由一个base class析构函数进行删除，这导致了生成的派生类对象在内存中没有被销毁，造成”局部销毁“。

解决办法：给基类一个virtual　析构函数，任何class只要带有virtual函数都几乎确定应该也有一个virtual析构函数。

如果class不含有virtual 函数，通常表示这个类并不会当做基类

想要实现出virtual函数，对象必须携带某种信息，这种信息用来在运行期间决定哪个virtual函数应该被调用。这份信息由一个vptr指针指出，vptr指向vtbl，每一个带有virtual函数的class都有一个相应的vtbl。vptr指针会增加对象50%-100%的空间。这样也会影响函数的移植性。

最好不要尝试集成标准容器或者一个”带有non-virtual析构函数“的class.

析构函数的调用方式：先调用最深层派生的那个累的析构函数，再一次调用每一个基类的析构函数。

<u>客制化</u>

### ８．别让异常逃离析构函数

析构函数吐出异常会导致程序过早结束或者出现不明确的行为，c++不鼓励析构函数吐出异常

两种方法避免析构函数中异常的传播

```c++
class DBConnection{
    public:
    	...
        static DBConnection creat();
    	void close();
};
class DBCon{
    public:
    	...
        ~DBCon()
        {
            db.close();
        }
    private:
    	DBConnection db;
};
```

１.调用abort函数，强迫结束程序

```c++
~PBCon()
{
    try{db.close();}
    catch(...){
        //制作运转记录，记下对close的调用失败
        std::abort();
    }
}
```

2. 吞下因调用close 而发生的异常PBCon(),　

```c++
~PBCon()
{
    try{db.close();}
    catch(...){
        //制作运转记录，记下对close的调用失败
    }
}
```

3.重新设计close接口,把调用close函数的责任转移到客户手上。（甩锅方法？？？）

```c++
class DBCon{
    public:
    	...
        void close(){
        	db.close();
            closed=true;
        }
   		 ~DBCon()
    	{
        	if(!closed)
        	{
            	try{db.close();}
            	catch(...){
                	//制作运转记录，记下调用失败；
                	...
            	}
        	}
    	}
    private:
    	DBConnection db;
    	bool closed
}
```

### 9. 绝不在构造和析构过程中调用virtual函数

基类构造期间virtual函数绝不会下降到派生类阶层，取而代之的是，对象的行为就像隶属基类一样

解决办法：确定构造函数和析构函数在对象构建和被销毁期间都不会调用virtual函数。

### 10. 令operator =　返回一个reference to *this

为了实现数学意义上的连锁赋值，采用右结合律

```c++
a& operator = (const a& rhs)
{
    ...
    return* this
}
```

适用于所有赋值相关运算，包括不限于+=, -=, *=等

### 11. 在operator = 中处理“自我赋值”

"自我赋值"发生在对象被赋值给自己时，注意“别名”导致的自我赋值

“别名”：　有一个以上的方法指称某对象，一般而言如果某段代码操作pointers 或者reference而他们被用来”指向多个相同类型的对象“，就需要考虑这些对象是否为同一个，在派生中，甚至不需要声明为相同类型就可能造成别名

可行办法：在operator＝最前面进行一个”认同测试“达到”自我赋值“的检验目的

```c++
Ａ& A::operator=(const A & rhs)
{
    if(this == rhs) return *this;//认同测试
								 //如果是自我赋值，则不做任何事情    
    delete pb;//停止使用当前的bitmap;
    pb=new Bitmap(*rhs.pb);//使用rhs.bitmap的副本
    return *this;//
}
```

问题在于，这样解决了自我赋值的安全性，却无法解决异常安全性，如果new BItmap发生错误，则要花更多时间处置

因此，处理的重点转移到了对于异常的处理,通过合理的编排语句顺序，解决new带来的异常安全性，但是这样做不是最高效的方法

```c++
Ａ& A::operator=(const A & rhs)
{
   Bitmap* pOrig=pb;       //记住原先的pb
    pb=new Bitmap(*rhs.pb);//令pb指向*pb的一个副本
    delete pOrig;          //删除原先的pb
    return *this;
} 
```

另外一种 copy and swap 技术

```c++
A & A::opeator=(const A& rhs)
{
    A tmep(rhs);//复制rhs数据
    wasp(temp);//将*this和上述的复件的数据进行交换
    return *this;
}
```

### 12. 复制对象时不要忘记它的每个成分
自己在编写拷贝构造函数和重构赋值运算符时，如果此时在class里面添加了新的成员变量，那么要同时修改拷贝拷贝构造函数和赋值运算符。否则就会成为局部拷贝。

编写copying 函数时，要确保赋值所有的成员变量，并且派生类需要调用适当的基类的拷贝构造函数

不要尝试以拷贝构造函数实现赋值函数，也不要尝试以赋值函数实现拷贝构造函数，最好的做法是将两者共同的代码部分放进第三方成员函数中供这两个函数调用。

## 3.资源管理

常见资源包括不限于：动态分配内存，文件描述器，互斥锁，数据库连接，图形界面中的字型和笔刷，网络sockets等，当不使用这些资源时，必须将它**还**给系统。

### 13.以对象管理资源

 资源泄露发生的情况: 过早地触发return 语句或者continue, goto语句导致过早退出，或者在释放资源前触发了异常。

delete 语句

把资源放进对象，利用析构函数的自动调用机制确保资源被释放

C/C++定义了4个内存区间：代码区，全局变量与静态变量区，局部变量区即栈区，动态存储区，即堆（heap）区或自由存储区（free store）

智能指针 — auto_ptr， 不能让多个auto_ptr同时指向同一对象，否则会引发未定义行为。auto_ptr有一个性质可以预防这个问题：如果通过拷贝构造函数或者赋值操作符复制它们，它们会变成null, 复制得到的指针会取得资源的唯一拥有权利，由上可知auto_ptr无法进行正常的复制行为，注意它可以使用的范围



```c++
class Investment {...};
Investment* createInvestment();工厂函数，返回对象指针。
void f()
{
    std::auto_ptr<Investment>pInv(createInvestmenr( ));
    										//调用factory函数
    ...										//使用pInv 
}//利用auto_ptr的析构函数自动删除pInv
```

以对象管理资源体现了这么一种思想：资源取得的实际就是初始化实际（Resource Acquisition Is Initialization）在取得这个资源的同时用它初始化某个管理对象（在这里管理对象就是auto_ptr），然后在不需要资源的时候管理对象会自动调用析构函数确保资源被释放，在这中间，如果资源释放的动作可能会导致异常，那么可能需要参考条款8设计管理对象的析构函数

可以用引用计数型智慧指针（RCSP）持续追踪共有多少对象指向某一个资源，并在无人指向它时自动删除该资源，行为类似于垃圾回收机制

```c++
class Investment {...};
Investment* createInvestment();工厂函数，返回对象指针。
void f()
{
    std::tr1::shared_ptr<Investment>pInv1(createInvestmenr( ));
    										//调用factory函数
  	std::tr1::shared_ptr<Investment>pInv2(pInv1);//pInv1和pInv2同时指向一个对象
    pInv3=pInv1;
    ...										//使用pInv 
        
}//利用shared_ptr的析构函数自动删除pInv1和pInv2，pInv3，它们指向的对象也就被销毁
```

谨记：shared_ptr和auto_ptr不是万能的。

### 14.在资源管理类中小心 *copying* 行为（不是很理解）

对不是heap-based的资源，条款13中所述的智能指针一般不适合作为资源掌管者，这时需要建立自己的资源管理类。

资源的coyonmg 行为决定了RAII对象的copying行为

一般当一个RAII被复制时，常见的处理方式有2种：1. 禁止复制，把copy操作声明为private  2.对底层资源采用“引用计数法”，其他行为： 3. 深拷贝 4.转移底部资源的拥有权，把资源的所有权从被复制物转移到目标物。

### 15.在资源管理类中提供对原始资源的访问

### 16. 成对使用new和delete时要采用相同形式　

简而言之，就是在使用new动态分配对象时，相应的就要使用delete删除对象

如果在new表达式中使用[],那么相应的delete表达式也要使用[].

### 17. 以独立语句将newed对象置入只能指针

```c++
int priority();
void processWidget(std::tr1::shared_ptr<Widget> pw, int priority);
```

如果考虑调用processWidget

```c++
processsWidget(new Widget, priority());
```

无法通过编译，原因在于Widget对应的构造函数是一个explict构造函数，无法进行隐式转换，将`new Widget`的原始指针转换为`std::tr1::shared_ptr`

但是如果

```c++
processsWidget(std::tr1::shared_ptr<Widget>(new Widget), priority());
```

虽然可以通过编译，但是会由于后面函数调用的异常，是的new返回的指针丢失

因此，最好的办法是分开写，也即

```c++
std::tr1::shared_ptr<Widget>(new Widget)
processsWidget(pw, priority());
```

effective c++的学习先告一段落，没事再看，现在开始学习linux和计算机网络

# Linux学习



鸟哥的私房菜（基础学习） 

操作系统: 1. 每个操作系统都有一个内核，主要用于管控硬件并提供相关的能力，内核是常驻在内存的(开机)，2. x系统调用也即操作系统提供的一整套系统的开发接口

linux内的所有数据都是以文件的形态存在的，目录树

`date`显示日期, `cal`显示日历，`bc`计算器　`[Ctrl]+c`终止当前命令`[Ctrl]+d`退出

终端 内嵌入了命令解释器 `shell`, `cat /etc/shells`查看系统内可用的shell, `echo $SHELL`查看当前shell，　bash和shell的作用是一样的

命令和路径,文件名补齐`Tab`,一次(文件不止一个)和两次(显示全部)的区别

|   功能    |  快捷键   | 助记             |
| :-------: | :-------: | ---------------- |
|    上     | Ctrl - p  | previous         |
|    下     | Ctrl - n  | next             |
|    左     | Ctrl - b  | backward         |
|    右     | Ctrl - f  | forward          |
|    Del    | Ctrl - d  | delete光标后面的 |
|   Home    | Ctrl - a  | the first letter |
|    End    | Ctrl - e  | end              |
| Backspace | Backspace | delete           |
|   清除    | Ctrl - u  | 清除光标所有的行 |
| 终止命令  | Ctrl - c  |                  |

linux的目录结构　`cd ..` 回到上一级目录　`pwd`　查看当前目录

`bin`存放可执行文件，可以进入，然后执行相应的文件，也可以直接在终端内输入bin内的可执行文件名，两者的执行结果一致，但是过程有差别(shell命令解析)

`boot`存放系统启动程序

`dev`存放设备linux系统中所见皆文件，包括硬件设备（对应某个文件）

`home`存放用户

`lib`存放一些系统库文件比如c++的库

`media`跟外接磁盘相关

`root`管理员宿主目录进去先切换用户

`sudo su`退出用在

`use`存放用户安装的软件和资源　　

`etc`存放用户信息和系统配置文件

相对路径和绝对路径 cd . cd .. cd -   cd ~

mkdir　创建文件夹  后面添加文件夹名　

`ls`浏览文件夹内的所有文件　ls -a 显示隐藏文件　ls -d　显示目录 ls - Rl 递归进入

`touch` 创建一个空文件

文件类型：１普通文件`-`表示　２目录文件`d`表示　３字符设备文件`c`表示　４块设备文件`b`表示　５软连接文件`l`（硬链接文件归于普通文件）6管道文件`p`表示　７套接字`s` 8 未知文件

which　查看指定命令路径

pwd　　查看当前文件目录

rmdir　删除空目录

rm  -rf　强制删除(慎重慎重慎重又慎重)

cp 拷贝文件到某个文件夹　-a(all)) , -d  -r

`cat`查看文件内容，读终端输入　　　`tac`倒序查看文件

`more`  查看文件　分屏显示　 `less`   　分屏显示　`head` 显示默认前十行，可以指定参数　　`tail`显示默认后十行

`tree`　需要下载安装，按照结构树的显示

`wc` `od`

软连接和硬链接　`ln`

软连接　ln -s  file file.s 给file文件创建一软连接，类似与windows的快捷方式，存放链接文件的访问路径　　如果要保证创建的软连接在任何地方都可以用，需要用绝对路径。软连接对源文件具有完全的读写权限

硬连接　对硬连接其中的文件任意一个修改，那么硬连接的文件都会修改，每个文件都有唯一的Inode, 修改的时候会彼此同步，删除的时候只把硬连接基数-1，减到０时，Inode被释放

`stat`查看文件状态

`mv`移动文件

`whoami`显示当前用户

`chmod`修改文件属性（读写执行权限）两种设定方法，文字设定法，数字设定法（４　２　１每一用户对应权限数字加起来就可以 `chmod [who][+|-|=] [mode] 文件名` a :all u:usr　g :同组用户　o:其他用户 r：读　w：写　x: 执行

`chown` 更改文件所有者

创建用户，创建用户组，suso　adduser|addgroup +用户名｜组名

chown和chgrp修改文件所有者和用户组

chown也可以一次性修改完文件所属用户和用户组用`:`分开用户名和用户组

删除用户和组把add替换成del就可以了

查找与检索

linux不以文件后缀名区分文件类型，而是以文件读写权限区分

`find`　默认磁盘块大小,以文件为搜索对象

块的大小是512字节，概念来源于磁盘，均分扇区（磁盘划分的最小区域）最小分区单位

`find -type`按文件类型搜索 d/p/s/c/b/l   f:文件

 `find ./ '*.cpp'`在当前文件内寻找后缀为cpp的文件（包括子目录）

`find ./ -maxdepth 1 -name '*.cpp'`搜集层级深度为１, maxdepth和name不能互换位置

`find ./ -size +20M -size -50M　　　`　按照文件大小搜索(大于20ｍ,小于50ｍ)　单位 k, M, G(大小写不一样)

`-atime  -ctime(修改时间，按天计算)   -mtime   `　　　`-amin  -cmin(修改时间，按分钟计算)   -mmin`

`find /usr/ -name "*tmp*" -exec ls -l {} \;`　　`{}`表示`find /usr/ -name "*tmp*"`   `\;`表示命令行的结束  `-exec`将find搜索的结果执行某一个指定的命令

`find /usr/ -name "*tmp*" -ok ls -l {} \;`将find搜索的结果执行某一个指定的命令，并且会询问

`find ./ maxdepth 1 -type f | xargs ls -l`不加xargs管道|是没有用的，结果显示的是ls -l 的结果

`xargs`对管道之前的任务进行分片处理，再交给管道后面的命令执行，比-exec的效率要高一些，把找到的文件名按照空格进行区分（小缺陷），解决办法是加入`-print0 | xargs　-print0 `强制用０进行拆分

`-exec`同一把管道前面的任务一起直接交给管道后面的命令执行

`grep` 找文件内容

`grep -r 'class' ./ -n` `-r`递归参数　`-n`显示内容所在行数

`ps`监控后台工作进程　`ps aux`类似于windows的任务管理器　　`ps aux | grep ‘hao’`检索进程内容为hao的进程，如果hao不存在，那么搜到的结果是关于grep，且只有一条信息　

管道

`touch abc xyz` 创建两个文件　`touch abc\ xyz`创建一个文件名字为`abc xyz`

 `awk` `sed` 结合正则表达式使用，脚本编程　　书籍下载`sed与awk　第三版`

安装卸载软件

`sudo` 超级管理员权限

`apt-get` 

软件源:`sudo apt-get update`　获取本地软件源列表到本地，`sudo apt-get install　softeare`安装、

卸载　`sudo  apt-get remove software`

deb包安装，ubuntu内所有软件安装包都是`.deb`格式,，等价于`.exe`

安装`sudo dpkg -i xxx.deb`

卸载`sudo apt-get remove software`或者`sudo dpkg  -r xxx.deb` 

原码安装

1. 解压 
2. cd dir 
3. 检查文件是否缺失，用configure创建Makefile,检测编译环境
4. 用make编译原码，生成库和可执行程序
5. 把库和可执行程序，安装到系统路径下　`sudo make install`
6. `sudo make distclean`卸载和删除软件

压缩包管理

１．`tar -zcvf 要生成的压缩包名　压缩材料`（z,gzip，c创建，v显示压缩过程）

`gzip`和`gunzip`只能压缩一个文件

`tar`用于打包文件　

２．bzip2跟gzip很像　`tar -jcvf 要生成的压缩包名　压缩材料`

３．解压　`tar -zxvf 要生成的压缩包名　压缩材料`  `tar -jxvf 要生成的压缩包名　压缩材料`

4. 压缩`rar a -r 压缩目标文件名　原文件`　解压`unrar x 压缩文件`
5. aptitude　有一个show命令可以查看文件安装状态，和apt-get类似
6. `zip -r 压缩包名　原文件`  解压　`unzip 压缩包名`

进程管理相关命令

1`who`查看当前电脑用户，带有进程

２　`ps`

３．`jobs`

４．`env`

5. `top` 文字版的任务管理器
6. 

设置密码

sudo passwd 用户名修改用户密码

７．root用户，`sudo su`变成root用户，不要使用

８．删除用户　

９．　`ifconfig`查看网卡信息

10. `man` 帮助手册
11. `umask [-p] -S [mode]`
12. `date`查看时间

`vim`

１. 三种工作模式　命令模式，文本模式（编辑模式）　末行模式, 命令模式转化成文本模式有i, I, a, A,o ,O,s,S等按键进入编辑模式，编辑模式和末行模式不能直接转换，　编辑模式进入命令模式`Esc`摁键，命令模式进入末行模式`:`,末行模式`w`保存，`q`退出，命令模式直接退出`shift+ZZ`　，末行模式进入命令模式`	Esc`摁两次就可以，或者执行末行命令

２．`i 插入光标前一个字符`，`I插入行首`，`a插入光标后一个人字符`, `A插入行末`, `s向下新开一行，插入行首`，`O向上新开一行，插入行首`

３. 光标移动`h向左j向下k向上l向右`

４．跳转到指定行:1 