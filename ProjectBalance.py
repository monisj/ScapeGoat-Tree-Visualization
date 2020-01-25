import math
import igraph
from igraph import Graph, EdgeSeq
import plotly.graph_objects as go
node_value=0
node_list=[]
sorted_node=0


import wx
import wx.xrc
class MyFrame1 ( wx.Frame ):
    def __init__( self, parent ):
        
            wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"ScapeGoat Tree", pos = wx.DefaultPosition, size = wx.Size( 1280,720 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

            self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
            bSizer1 = wx.BoxSizer( wx.VERTICAL )
            self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"ScapeGoat Tree Visualiser", wx.DefaultPosition, wx.DefaultSize, 0 )
            self.m_staticText1.Wrap( -1 )
            bSizer1.Add( self.m_staticText1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
            self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Click this bottom button for an tree visualization example", wx.DefaultPosition, wx.DefaultSize, 0 )
            self.m_staticText4.Wrap( -1 )

            bSizer1.Add( self.m_staticText4, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

            self.m_button4 = wx.Button( self, wx.ID_ANY, u"Tree", wx.DefaultPosition, wx.DefaultSize, 0 )
            bSizer1.Add( self.m_button4, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        

            self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Click this bottom Button for ScapeGoat Balanced Tree Example", wx.DefaultPosition, wx.DefaultSize, 0 )
            self.m_staticText3.Wrap( -1 )

            bSizer1.Add( self.m_staticText3, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

            self.m_button3 = wx.Button( self, wx.ID_ANY, u"Scapetree", wx.DefaultPosition, wx.DefaultSize, 0 )
            bSizer1.Add( self.m_button3, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

            self.m_staticText13 = wx.StaticText( self, wx.ID_ANY, u"Click this bottom Button for Creating an unsorted Binary Tree", wx.DefaultPosition, wx.DefaultSize, 0 )
            self.m_staticText13.Wrap( -1 )

            bSizer1.Add( self.m_staticText13, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

            self.m_button13 = wx.Button( self, wx.ID_ANY, u"Create Tree", wx.DefaultPosition, wx.DefaultSize, 0 )
            bSizer1.Add( self.m_button13, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

            self.m_staticText33 = wx.StaticText( self, wx.ID_ANY, u"Click this bottom Button for Visualising your ScapeGoat Tree", wx.DefaultPosition, wx.DefaultSize, 0 )
            self.m_staticText33.Wrap( -1 )

            bSizer1.Add( self.m_staticText33, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

            self.m_button33 = wx.Button( self, wx.ID_ANY, u"Show Tree", wx.DefaultPosition, wx.DefaultSize, 0 )
            bSizer1.Add( self.m_button33, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


            bSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )


            bSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )


            self.SetSizer( bSizer1 )
            self.Layout()

            self.Centre( wx.BOTH )

            # Connect Events
            self.m_button33.Bind( wx.EVT_BUTTON, self.ShowTree)
            self.m_button13.Bind( wx.EVT_BUTTON, self.CreateTree)
            self.m_button4.Bind( wx.EVT_BUTTON, self.Tree )
            self.m_button3.Bind( wx.EVT_BUTTON, self.ScapeTree )
            self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)

    def __del__( self ):
            pass


    # Virtual event handlers, overide them in your derived class
    def ShowTree(self,event):
        print("The list has value =",sorted_node)
        if sorted_node==0:
            frame=MyFrame30(None).Show()
        else:
            frame=MyFrame70(None).Show()
    
    def CreateTree(self,event):
        frame=MyFrame20(None).Show()
        
    
    def Tree( self, event ):
            frame=MyFrame3(None).Show()

    

    def ScapeTree( self, event ):
            frame=MyFrame2(None).Show()

    def OnEraseBackground(self, evt):
            dc = evt.GetDC()
            if not dc:
                dc = wx.ClientDC(self)
                rect = self.GetUpdateRegion().GetBox()
                dc.SetClippingRect(rect)
            dc.Clear()
            bmp = wx.Bitmap(u"../project/Piran_Technologies_Networking_Outsourced_IT_ServicesCornwall_2017_2023.jpg")
            dc.DrawBitmap(bmp, 0,0)

class MyFrame70 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 900,700 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		self.m_bitmap1 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"C:\\Users\\koolm\\Desktop\\project\\udoscape.dot.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.m_bitmap1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_button2 = wx.Button( self, wx.ID_ANY, u"Close", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.m_button2, 0, wx.ALL, 5 )


		bSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer2 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button2.Bind( wx.EVT_BUTTON, self.close )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def close( self, event ):
		self.Close()

class MyFrame30 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 300,80 ), style = 0|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"The List Is Empty Click the Above Button To Create It", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		bSizer1.Add( self.m_staticText1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_button1 = wx.Button( self, wx.ID_ANY, u"Return", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.m_button1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button1.Bind( wx.EVT_BUTTON, self.Return )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def Return( self, event ):
		self.Close()




class MyFrame2 ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 800,600 ), style = 0|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer2 = wx.BoxSizer( wx.VERTICAL )

        self.m_bitmap1 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"../project/udo.dot.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer2.Add( self.m_bitmap1, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )

        self.Button2 = wx.Button( self, wx.ID_ANY, u"Close", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer2.Add( self.Button2, 0, wx.ALL, 5 )


        self.SetSizer( bSizer2 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.Button2.Bind( wx.EVT_BUTTON, self.GoBack )
        self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)

    def __del__( self ):
        pass


    # Virtual event handlers, overide them in your derived class
    def GoBack( self, event ):
        self.Close()

    def OnEraseBackground(self, evt):
            dc = evt.GetDC()
            if not dc:
                dc = wx.ClientDC(self)
                rect = self.GetUpdateRegion().GetBox()
                dc.SetClippingRect(rect)
            dc.Clear()
            bmp = wx.Bitmap(u"../project/opnl_1_786px.jpg")
            dc.DrawBitmap(bmp, 0,0)
 

class MyFrame3 ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 800,600 ), style = 0|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer2 = wx.BoxSizer( wx.VERTICAL )

        self.m_bitmap1 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"../project/udo2.dot.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer2.Add( self.m_bitmap1, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )

        self.Button2 = wx.Button( self, wx.ID_ANY, u"Close", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer2.Add( self.Button2, 0, wx.ALL, 5 )


        self.SetSizer( bSizer2 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.Button2.Bind( wx.EVT_BUTTON, self.GoBack )
        self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)

    def __del__( self ):
        pass


    # Virtual event handlers, overide them in your derived class
    def GoBack( self, event ):
        self.Close()

    def OnEraseBackground(self, evt):
                dc = evt.GetDC()
                if not dc:
                    dc = wx.ClientDC(self)
                    rect = self.GetUpdateRegion().GetBox()
                    dc.SetClippingRect(rect)
                dc.Clear()
                bmp = wx.Bitmap(u"../project/hello.jpg")
                dc.DrawBitmap(bmp, 0,0)

class MyFrame20 ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer1 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Enter no of nodes to be Inserted", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText1.Wrap( -1 )

        bSizer1.Add( self.m_staticText1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.m_textCtrl1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_TAB )
        bSizer1.Add( self.m_textCtrl1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Enter The Tree Nodes any order", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText4.Wrap( -1 )

        bSizer1.Add( self.m_staticText4, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.m_textCtrl3 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer1.Add( self.m_textCtrl3, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.m_button1 = wx.Button( self, wx.ID_ANY, u"Submit", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer1.Add( self.m_button1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


        self.SetSizer( bSizer1 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.m_button1.Bind( wx.EVT_BUTTON, self.GoSubmit )

    def __del__( self ):
        pass


    # Virtual event handlers, overide them in your derived class
    def GoSubmit( self, event ):
        ob1=self.m_textCtrl1.GetValue()#Value of No of Nodes
        ob2=self.m_textCtrl3.GetValue()#List of Nodes
        bd=ob1.isdigit()
        a=eval(ob2)
        bet=eval(ob1)
        if bd==False:
                    frame=MyFrame23(None).Show()
        elif bd==True:
            if ob2=="":
                frame=MyFrame24(None).Show()
            elif len(a)!=bet:
                frame=MyFrame15(None).Show()
            else:
                bd1=(isinstance(a,list))
                bd2=None
                print(bd1)
                if bd1==False:
                    frame=MyFrame25(None).Show()
                else:
                    print(ob2)
                    if a==[]:
                        frame=MyFrame15(None).Show()
                    else:
                        for i in range(len(a)):
                            bd=a[i]
                            bd=str(bd)
                            if bd.isdigit()==False:
                                print("The List has negative or alphabetic values")
                                bd2=False
                            break

        
                        if bd1==False:
                            frame=MyFrame24(None).Show()
                        elif bd1==True:
                            if bd2==False: 
                                frame=MyFrame24(None).Show()
                node_value=eval(ob1)
                node_list=eval(ob2)
                print(node_list)
                driver(node_list)
                self.Close()
                
class MyFrame15 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 300,80 ), style = 0|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"The Enter Node Value is Not Equal to Entered Nodes", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		bSizer1.Add( self.m_staticText1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_button1 = wx.Button( self, wx.ID_ANY, u"Return", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.m_button1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button1.Bind( wx.EVT_BUTTON, self.Return )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def Return( self, event ):
		self.Close()
        
                    
class MyFrame23 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 380,80 ), style = 0|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"The Value You Added For Nodes is either Negative or Alphabetic", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )

		bSizer2.Add( self.m_staticText5, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_button2 = wx.Button( self, wx.ID_ANY, u"Return", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.m_button2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.SetSizer( bSizer2 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button2.Bind( wx.EVT_BUTTON, self.Return )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def Return( self, event ):
		self.Close()
class MyFrame24 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 380,80 ), style = 0|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"The Value You Added For Nodes is either Negative or Alphabetic or Empty", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )

		bSizer2.Add( self.m_staticText5, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_button2 = wx.Button( self, wx.ID_ANY, u"Return", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.m_button2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.SetSizer( bSizer2 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button2.Bind( wx.EVT_BUTTON, self.Return )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def Return( self, event ):
		self.Close()

class MyFrame25 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 380,80 ), style = 0|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"The Value You Added For Nodes is integer or alphabetic not list", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )

		bSizer2.Add( self.m_staticText5, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_button2 = wx.Button( self, wx.ID_ANY, u"Return", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.m_button2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.SetSizer( bSizer2 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button2.Bind( wx.EVT_BUTTON, self.Return )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def Return( self, event ):
		self.Close()

class Node(object):
    def __init__(self,data=[]):
        self.data=data
        self.left=None
        self.right=None
        self.middle=None
        self.parent=None

    def is_leaf(self):
        if(self.left ==None and self.right ==None and self.middle ==None):
            return True
        assert (self.left ==None and self.right == None) or (self.left !=None and self.right !=None), "Invalid Node Found"
        return False

    def is_branch(self):
        if(self.is_leaf()):
            return False
        elif(len(self.data)==1):
            assert(self.middle ==None), "Invalid Node Found"
            assert (self.left !=None and self.right !=None), "Invalid Node Found"
        elif(len(self.data)==2):
            assert self.left != None and self.right!=None and self.middle !=None,"Invalid Node Found"
        return True

    def insert(self,item):
        if(len(self.data) > 2):
            raise ValueError("Too Many Values in Node cannot insert")
        self.data.append(item)
        self.data.sort()
        return

class Tree23(object):
    def __init__(self,items=[]):
        self.root=None
        for item in items:
            self.add(item)

    def add(self,item):
        if(self.root is None):
            self.root=Node([item])
            return
        node=self.findValidNode(item,self.root)
        assert node.is_leaf(),"Invalid Node for adding item"
        node.insert(item)
        self.balance(node)
        return

    def findValidNode(self,item,node):
        assert node is not None,"Given node with None Value"

        if(node.is_leaf()):
            return node
        direction=self.getDirection(item,node)
        if(direction =="left"):
            return self.findValidNode(item,node.left)
        elif(direction=="right"):
            return self.findValidNode(item,node.right)
        elif(direction =="middle"):
            return self.findValidNode(item,node.middle)
        assert node.is_leaf(),"Invalid node,its not a leaf"
        return node

    def getDirection(self,item,node):
        assert node.is_branch(),"Cannot get direction for leaf node"
        if(len(node.data)==1):
            if(item<node.data[0]):
                return "left"
            elif(item>node.data[0]):
                return "right"
            elif(item==node.data[0]):
                raise ValueError("Duplicated not allowed -YET-")
        elif(len(node.data==2)):
            if(item<node.data[0]):
                return "left"
            elif(item>node.data[1]):
                return "right"
            elif(node.data[0]<item<node.data[1]):
                return "middle"
            elif(item==node.data[0] or item==node.data[1]):
                raise ValueError("Duplicated not allowed -YET-")
        raise ValueError("Invalid Node")

    def balance(self,node):
        if(len(node.data)<3):
            return
        if(node.parent is None and node.is_leaf()):
            self.balance1(node)
            return
        direction =self.getDirection(node.data[0],node.parent)
        if(direction =="middle"):
            self.balance4(node)
        elif(node.middle is not None):
            self.balance3(node,direction)
            self.balance(node.parent)
        else:
            self.balance2(node,direction)
            self.balance(node.parent)
    def balance1(self,node):
        if(len(node.data)<3):
            return
        assert node.is_leaf(),"Why are you balancing a branch?"
        min_elem=node.data.pop(0)
        left=Node([min_elem])
        max_elem=node.data.pop()
        right=Node([max_elem])
        assert len(node.data)==1,"Data pops did not work?"
        left.prev=node
        right.prev=node
        node.left=left
        node.right=right
        assert node.is_branch(),"Balanced,but not a branch?"
        return

    def balance2(self,node,direction):
        mid_elem=node.data.pop(1)
        node.parent.data.insert(mid_elem)
        if(node.parent.middle is None):
            node.parent.middle=Node()
        if(direction=="left"):
            node.parent.middle.insert(node.data.pop())
        elif(direction=="right"):
            node.parent.middle.insert(node.data.pop(0))
        return

    def balance3(self,node,direction):
        temp=Node(node.data)
        self.balance1(temp)
        temp.left.left=node.left
        temp.right.right=node.right
        temp.left.right=Node([node.middle.data[0]])
        temp.right.left=Node([node.middle.data[1]])
        if(node.parent is None):
            self.root=temp
            return
        temp.prev=node.prev
        if(direction=="left"):
            temp.prev.left=temp
        elif(direction=="right"):
            temp.prev.right=temp
        elif(direction=="middle"):
            temp.prev.middle=temp
        node=temp
        return

    def balance4(self,node):
        parent=node.parent
        temp=Node(parent.data)
        temp.parent=parent.parent
        mid_elem=node.data.pop(1)
        temp.inset(mid_elem)
        self.balance1(temp)
        
        parent.left.parent=temp.left
        temp.left.left=parent.left
        parent.right.right=temp.right
        temp.right.right=parent.right

        temp.left.right=Node([node.data.pop(0)])
        temp.left.right.parent=temp.left.right
        temp.right.left=Node([node.data.pop()])
        temp.right.left.parent=temp.right.left

        node=temp
        if(temp.parent is None):
            self.root=temp
        return

    def findHelper(self,item,node):
        if(node is None):
            return False
        for elem in node.data:
            if(item==elem):
                return True
        direction=self.getDirection(item,node)
        if(direction=="left"):
            return self.findHelper(item,node.left)
        elif(direction=="right"):
            return self.findHelper(item,node.right)
        elif(direction=="middle"):
            return self.findValidNode(item,node.middle)
        return False

    def find(self,item):
        return self.findHelper(item,self.root)

    def printTreeHelper(self,node):
        if(node==None):
            return
        self.printTreeHelper(node.left)
        print(node.data[0])
        if((node.data[0])==2):
            self.printTreeHelper(node.middle)
            print(node.data[0])
        self.printTreeHelper(node.right)
        return

    def printTree(self):
        return self.printTreeHelper(self.root)

    def getSortedTree(self,node,result):
        if(node==None):
            return
        self.getSortedTree(node.left,result)
        result.append(node.data[0])
        if(len(node.data)==2):
            self.getSortedTree(node.middle,result)
            result.append(node.data[1])
        self.getSortedTree(node.right,result)
        return

    def sortedTree(self):
        result=[]
        self.getSortedTree(self.root,result)
        return result
    
    def buildTreeFromSortedList(self,dumylist,node23,nodes, start, end):
        if start > end:
            return None
        mid = int(math.ceil(start + (end - start) / 2.0))
        node = nodes[mid]
        x=self.root
        if self.root is None:
            self.root=node
            b="Root",node
            dumylist.append(b)
        else:
            if node>x.data[0]:
                if node>node23[-1]:
                    node23.append(node)
                    b="RRight",node
                    dumylist.append(b)
                elif node<node23[-1]:
                    b="LRight",node
                    dumylist.append(b)
                    node23.append(node)
            elif node<x.data[0]:
                if node>node23[-1]:
                    b="RLeft",node
                    dumylist.append(b)
                    node23.append(node)
                elif node<node23[-1]:
                    b="LLeft",node
                    dumylist.append(b)
                    node23.append(node)
        self.buildTreeFromSortedList(dumylist,node23,nodes,start,mid-1)
        self.buildTreeFromSortedList(dumylist,node23,nodes, mid+1, end)
        return node23
def treemake(lis):
    global sorted_node
    #Driver Code
    print(lis)
    items=list(set(lis))
    print("Sorted tree  items are =",str(items))
    tree=Tree23(items)
    result=tree.sortedTree()
    print("The Result is =")
    print(result)                                                  ###################################
    a=result                                                       #Test Driver Code uncomment all lines for testing purposes
    b=len(result)                                                  #If you want to see balanced scapegoat tree
    mid = int(math.ceil(0 + (b-1 - 0) / 2.0))                      ###################################
    node23=[]
    bd=result[mid]
    bc=[]
    bc.append(bd)
    tree1=Tree23(bc)
    bt=bd
    node23.append(bt)
    bt=("Root",bd)
    dumylist=[]
    dumylist.append(bt)
    d=tree1.buildTreeFromSortedList(dumylist,node23,result,0,len(result)-1)
    print("Nodes with list =",dumylist)
    print(d)
    sorted_node=d
    makeedge(d)
def driver(lis):
    treemake(lis)


def treeplot(edge):
    #Tree
    from anytree import Node, RenderTree
    from anytree.exporter import DotExporter
    from graphviz import Source
    from graphviz import render
    import os

    os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'
    
    def plot2(edge):
        bt=[]
        br=[]
        tree21=edge[0][0]
        edge1=edge
        index=0
        if br==[]:
            br.append(tree21)
            udo=Node(tree21)
            bt.append(udo)
        for i in edge1:
            t=i[0]
            p=i[1]
            if t in br:
                for i in range(len(edge1)):
                    if i<len(edge1):
                        t2=edge1[i][1]
                        if t2==t:
                            t1=edge1[i+1][0]
                            if t1==t:
                                print(i+1)
                                index+=(i+1)
                print(index)
                print(br)
                t=Node(p,parent=bt[index])
                bt.append(t)
                index=0
            elif t  not in br:
                br.append(t)
                t=Node(p,parent=bt[-1])
                bt.append(t)

        for pre, fill, node in RenderTree(udo):
             print("%s%s" % (pre, node.name))

        DotExporter(udo).to_dotfile('udoscape.dot')
        Source.from_file('udoscape.dot')
        render('dot','png','udoscape.dot')
    plot2(edge)
def makeedge(sorted_n):
    b=[]
    a=sorted_n
    c=[]
    for i in range(1,len(a)):
        c.append(a[i])
    d=[]
    e=[]
    print(a)
    print(c)
    d.append(a[0])
    e.append(a[0])
    for i in range(len(c)):
        if c[i]<a[0]:
            if c[i]<a[i]:
                b.append([a[i],c[i]])
                d.append(c[i])
            elif c[i]>a[i]:
                for j in range(len(d)-1,-1,-1):
                    if d[j]>c[i]:
                        b.append([d[j+1],c[i]])
                        break
        if c[i]>a[0]:
            if len(e)==1:
                b.append([a[0],c[i]])
                e.append(c[i])
            elif c[i]<a[i]:
                b.append([a[i],c[i]])
                e.append(c[i])
            elif c[i]>a[i]:
                for j in range(len(e)-1,-1,-1):
                    if e[j]>c[i]:
                        b.append([e[j],c[i]])
                        e.append(c[i])
                        break
                    elif j==0:
                        b.append([e[-1],c[i]])
                        e.append(c[i])
    print(b)
    print(d)
    print(e)
    treeplot(b)



app=wx.App()
frame=MyFrame1(None).Show()

app.MainLoop()
