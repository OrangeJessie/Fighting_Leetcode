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