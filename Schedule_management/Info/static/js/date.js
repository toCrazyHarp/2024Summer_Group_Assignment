function updateTime() {
  const now = new Date();
  const year = now.getFullYear();
  const month = String(now.getMonth() + 1).padStart(2, '0'); // 月份从0开始，所以+1
  const day = String(now.getDate()).padStart(2, '0');

  // 假设您有一个函数来滚动显示数字，这里我们只是简单地将它们设置到DOM中
  // 实际情况中，您可能需要使用更复杂的逻辑或库来实现滚动效果
  document.getElementById('dateDisplay').textContent = `${year}-${month}-${day}`;

  // 递归调用以每秒更新时间
  setTimeout(updateTime, 1000);
}

// 初始调用
updateTime();