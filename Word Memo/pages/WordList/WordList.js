// pages/WordList/WordList.js
const app =getApp();
Page({

  /**
   * 页面的初始数据
   */
  data: {
    userinfo: "",
    openid: "",
    session_key: "",
    level:'',
    inputValue: '',
    word_translation:[],
  },
  bindKeyInput: function (e) {
    this.setData({
      inputValue: e.detail.value
    })
    console.log(this.data.inputValue)
  },
  todetail:function(e){
    let word = e.currentTarget.dataset.word;
    let translation = e.currentTarget.dataset.translation;
    wx.navigateTo({
      url: '../WordDetail/WordDetail?word='+word+'&translation='+translation,
    })
  },
  tapsearch:function(){
    var that = this;
    wx.request({
      url: app.globalData.server_url,
      method:'post',
      dataType:"json",
      data:{
        eType:'GetMemoWord',
        edetail:{
          openid:that.data.openid,
          level:that.data.level,
          word:that.data.inputValue,
          word_translation:null,
        }
      },
      success:function(res){
        var list = res.data.edetail["word_translation"]
        console.log(list)
        that.setData({
          word_translation:list,
        })
        console.log(that.data.word_translation)
      }
    })
  },
  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    console.log(options.level)
    var that = this;
    that.setData({
      level:options.level
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
        eType:'GetMemo',
        edetail:{
          openid:that.data.openid,
          level:that.data.level,
          word_translation:null,  
        }
      },
      success:function(res){
        var list = res.data.edetail["word_translation"]
        console.log(list)
        that.setData({
          word_translation:list,
        })
        console.log(that.data.word_translation)
      }
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