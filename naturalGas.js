window.onload=function() {
    var containerDiv = document.getElementById('ng'),
        url = "https://public.tableau.com/views/coalbytime/NaturalGasProportion?:language=en&:display_count=y&publish=yes&:origin=viz_share_link",
        options = {
        
            onFirstInteractive: function () {
                console.log("Run this code when the viz has finished loading.");
            }
        };

    var viz = new tableau.Viz(containerDiv, url, options);
    // Create a viz object and embed it in the container div.
}