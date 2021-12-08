// pages/Personal/Personal.js
const app =getApp();
Page({

  /**
   * 页面的初始数据
   */
  data: {
    userinfo: "",
    openid: "",
    session_key: "",
  },
  bindGetUserInfo: function () {
    var that = this;
    wx.getUserProfile({
      desc: '必须授权才可以继续使用',
      success: res => {
        let user = res.userInfo
        console.log(user)
        wx.login({
          success: function (res) {
            wx.request({
              //获取openid接口  
              url: app.globalData.server_url,
              dataType:"json",
              data: {
                eType:'GetID',
                edetail:{
                  js_code: res.code,
                  openid:null,
                  session_key:null,
                }
              },
              method: 'POST',
              success: function (res) {
                console.log(res.data)
                var OPEN_ID = res.data.edetail["openid"];//获取到的openid  
                var SESSION_KEY = res.data.edetail["session_key"];//获取到session_key  
                that.setData({
                  openid: OPEN_ID,
                  session_key: SESSION_KEY,
                  userinfo: user,
                })
                wx.setStorageSync('userinfo', user);
                wx.setStorageSync('openid', OPEN_ID);
                wx.setStorageSync('session_key', SESSION_KEY);
                wx.request({
                  url: app.globalData.server_url,
                  method:'post',
                  dataType:"json",
                  data:{
                    eType:'GetUser',
                    edetail:{
                      result:null,
                      openid:OPEN_ID,
                      session_key:SESSION_KEY,
                    }
                  },
                  success:function(res){
                    console.log(res.data.edetail["result"])
                  }
                })
              }
            })
          }
        })
      },
      fail: res => {
        console.log('授权失败')
      }
    })
  },
  logout: function () {
    wx.clearStorage({})
    wx.reLaunch({
      url: '../Personal/Personal',
    })
  },
  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function () {
    let user = wx.getStorageSync('userinfo')
    let openid = wx.getStorageSync('openid')
    let session_key = wx.getStorageSync('session_key')
    this.setData({
      userinfo: user,
      openid: openid,
      session_key: session_key,
    })
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