// pages/WordDetail/WordDetail.js
const app =getApp();
Page({

  /**
   * 页面的初始数据
   */
  data: {
    userinfo: "",
    openid: "",
    session_key: "",
    word:"",
    translation:"",
    icon_url:"",
    level:"",
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    var word = options.word;
    var translation = options.translation;
    var that = this;
    that.setData({
      word : word,
      translation : translation,
    })
    let user = wx.getStorageSync('userinfo')
    let openid = wx.getStorageSync('openid')
    let session_key = wx.getStorageSync('session_key')
    this.setData({
      userinfo: user,
      openid: openid,
      session_key: session_key,
    })
    wx.request({
      url: app.globalData.server_url,
      method:'post',
      dataType:"json",
      data:{
        eType:'FindMemo',
        edetail:{
          openid:that.data.openid,
          word:that.data.word,
        }
      },
      success:function(res){
        console.log(res.data.edetail["result"])
        if(res.data.edetail["result"] === "easy"||res.data.edetail["result"] === "mid"||res.data.edetail["result"] === "hard"){
          that.setData({
            icon_url:"/pages/images/delete.png",
            level:res.data.edetail["result"]
          })
          console.log(that.data.level)
        }
        else if(res.data.edetail["result"] === "none"){
          that.setData({
            icon_url:"/pages/images/star.png"
          })
        }
      }
    })
  },
  tapstar:function(){
    var that = this;
    if(that.data.icon_url ==="/pages/images/delete.png"){
      wx.request({
        url: app.globalData.server_url,
        method:'post',
        dataType:"json",
        data:{
          eType:'DeleteMemo',
          edetail:{
            result:null,
            openid:that.data.openid,
            word:that.data.word,
            level:that.data.level,
          }
        },
        success:function(res){
          var result = res.data.edetail["result"]
          console.log(result)
          if(result === 'delete'){
            that.setData({
              icon_url:"/pages/images/star.png",
            })
          }
        }
      })
    }
    else if(that.data.icon_url ==="/pages/images/star.png"){
      var levellist = ['easy', 'mid', 'hard'];
      wx.showActionSheet({
        itemList: ['简单', '中等', '困难'],
        success: function (res) {
          if (!res.cancel) {
            console.log(res.tapIndex)//这里是点击了那个按钮的下标
            var level = levellist[res.tapIndex]
            wx.request({
              url: app.globalData.server_url,
              method:'post',
              dataType:"json",
              data:{
                eType:'InsertMemo',
                edetail:{
                  result:null,
                  openid:that.data.openid,
                  word:that.data.word,
                  level:level,
                }
              },
              success:function(res){
                var result = res.data.edetail["result"]
                console.log(result)
                that.setData({
                  icon_url:"/pages/images/delete.png",
                  level:level,
                })
              }
            })
          }
        }
      })
    }
  },

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {

  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {

  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide: function () {

  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload: function () {

  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function () {

  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function () {

  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {

  }
})