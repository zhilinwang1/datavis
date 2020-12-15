window.onload=function() {
    var containerDiv = document.getElementById('coal1'),
        url = "https://public.tableau.com/views/coalbytime/coal1?:language=en&:display_count=y&publish=yes&:origin=viz_share_link",
        options = {
        
            onFirstInteractive: function () {
                console.log("Run this code when the viz has finished loading.");
            }
        };

    var viz = new tableau.Viz(containerDiv, url, options);
    // Create a viz object and embed it in the container div.

    var containerDiv2 = document.getElementById('coal2'),
        url = "https://public.tableau.com/views/coalbytime/Coal3?:language=en&:display_count=y&publish=yes&:origin=viz_share_link",
        options = {
    
            onFirstInteractive: function () {
                console.log("Run this code when the viz has finished loading.");
            }
        };

    var viz2 = new tableau.Viz(containerDiv2, url, options);
    // Create a viz object and embed it in the container div.
}
