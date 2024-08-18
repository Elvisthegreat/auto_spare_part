// Function to get a random happiness message
function getRandomHappinessMessage() {
    const messages = [
        '<span style="color: red;">Quality auto spare parts are the backbone of any successful repair shop</span>',
        '<span style="color: blue;">In the world of auto repairs, having the right spare parts can make all the difference</span>',
        '<span style="color: green;">Auto spare parts are the unsung heroes that keep vehicles running smoothly</span>',
        '<span style="color: orange;">A well-stocked inventory of auto spare parts is essential for any mechanic</span>',
        '<span style="color: purple;">The auto spare parts industry is driven by innovation and precision</span>',
        '<span style="color: teal;">Finding the perfect auto spare part can be like finding a needle in a haystack, but it’s worth the effort</span>',
        '<span style="color: brown;">Auto spare parts are the building blocks of every vehicle on the road</span>',
        '<span style="color: pink;">The demand for high-quality auto spare parts is always on the rise</span>',
        '<span style="color: navy;">Auto spare parts suppliers play a crucial role in the automotive industry</span>',
        '<span style="color: maroon;">Investing in reliable auto spare parts can save time and money in the long run</span>',
        '<span style="color: olive;">The right auto spare part can breathe new life into an old vehicle</span>',
        '<span style="color: lime;">Auto spare parts are the key to maintaining the performance and safety of any car</span>',
        '<span style="color: cyan;">A successful auto repair business relies on a steady supply of top-notch spare parts</span>',
        '<span style="color: magenta;">The auto spare parts market is constantly evolving to meet the needs of modern vehicles</span>',
        '<span style="color: gold;">Choosing the right auto spare parts can make or break a repair job</span>',
      ];      
    return messages[Math.floor(Math.random() * messages.length)];
  }
  
  // Function to update the footer date and message
  function updateFooter() {
    const currentDate = new Date().toLocaleDateString("en-US", {
      weekday: "long",
      year: "numeric",
      month: "long",
      day: "numeric",
    });
    document.getElementById("footer-date").textContent =
      "Today is " + currentDate;
    document.getElementById("footer-message").innerHTML =
      getRandomHappinessMessage();
  }
  
  // Call updateFooter function when the page loads
  window.onload = updateFooter;

  // Update the message every minute
setInterval(() => {
    document.getElementById("footer-message").innerHTML =
      getRandomHappinessMessage();
  }, 6000);