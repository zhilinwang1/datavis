window.onload=function() {
    var containerDiv = document.getElementById('all'),
        url = "https://public.tableau.com/views/coalbytime/ElectricityProductionSourceProportionbytime?:language=en&:display_count=y&:origin=viz_share_link",
        options = {
        
            onFirstInteractive: function () {
                console.log("Run this code when the viz has finished loading.");
            }
        };

    var viz = new tableau.Viz(containerDiv, url, options);
    // Create a viz object and embed it in the container div.\
    var containerDiv2 = document.getElementById('pie'),
        url = "https://public.tableau.com/views/coalbytime/2015Prop?:language=en&:display_count=y&publish=yes&:origin=viz_share_link",
        options = {
        
            onFirstInteractive: function () {
                console.log("Run this code when the viz has finished loading.");
            }
        };

    var viz2 = new tableau.Viz(containerDiv2, url, options);
    // Create a viz object and embed it in the container div.\
    var containerDiv3 = document.getElementById('map'),
    url = "https://public.tableau.com/views/overview_16076996994530/MapOverviewof?:language=en&:display_count=y&publish=yes&:origin=viz_share_link",
    options = {
    
        onFirstInteractive: function () {
            console.log("Run this code when the viz has finished loading.");
        }
    };

var viz2 = new tableau.Viz(containerDiv3, url, options);
// Create a viz object and embed it in the container div.\

}
