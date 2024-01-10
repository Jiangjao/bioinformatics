var scrollContainer = document.querySelector(".scroll-container");
var scrollContent = document.querySelector(".scroll-content");
var scrollBar = document.querySelector(".scroll-bar");
var scrollThumb = document.querySelector(".scroll-thumb");

// 计算滑动条的高度
var contentHeight = scrollContent.offsetHeight;
var containerHeight = scrollContainer.offsetHeight;
var scrollBarHeight = (containerHeight / contentHeight) * containerHeight;
scrollThumb.style.height = scrollBarHeight + "px";

// 滚动内容时更新滑动条的位置
scrollContainer.addEventListener("scroll", function() {
    var scrollPercentage = scrollContainer.scrollTop / (contentHeight - containerHeight);
    var maxScroll = containerHeight - scrollBarHeight;
    var scrollBarPosition = maxScroll * scrollPercentage;
    scrollThumb.style.top = scrollBarPosition + "px";
});

// 拖动滑动块时更新内容的滚动位置
var isDragging = false;
var startY, startScrollTop;
scrollThumb.addEventListener("mousedown", function(event) {
    isDragging = true;
    startY = event.clientY;
    startScrollTop = scrollContainer.scrollTop;
});

document.addEventListener("mousemove", function(event) {
    if (!isDragging) return;

    var scrollDelta = event.clientY - startY;
    var maxScroll = containerHeight - scrollBarHeight;
    var contentDelta = (scrollDelta / maxScroll) * (contentHeight - containerHeight);
    scrollContainer.scrollTop = startScrollTop + contentDelta;
});

document.addEventListener("mouseup", function() {
    isDragging = false;
});