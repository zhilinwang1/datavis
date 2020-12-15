window.onload=function() {
    var containerDiv = document.getElementById('oil'),
        url = "https://public.tableau.com/views/coalbytime/Oilpvsrent?:language=en&:display_count=y&:origin=viz_share_link",
        options = {
        
            onFirstInteractive: function () {
                console.log("Run this code when the viz has finished loading.");
            }
        };

    var viz = new tableau.Viz(containerDiv, url, options);
    // Create a viz object and embed it in the container div.\
    var containerDiv2 = document.getElementById('oil2'),
        url = "https://public.tableau.com/shared/SZBH44B7G?:display_count=y&:origin=viz_share_link",
        options = {
        
            onFirstInteractive: function () {
                console.log("Run this code when the viz has finished loading.");
            }
        };

    var viz2 = new tableau.Viz(containerDiv2, url, options);
    // Create a viz object and embed it in the container div.\

}
