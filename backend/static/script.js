// ==============================
// ARCHETYPE DATA
// ==============================

const archetypes = [

{
symbol:"☼",
title:"The Luminary",
desc:"A presence that naturally draws attention and influences the emotional tone of environments."
},

{
symbol:"☾",
title:"The Empath",
desc:"Individuals who are naturally attentive to emotional atmosphere and relational dynamics."
},

{
symbol:"🏛",
title:"The Architect",
desc:"Builders of stable systems who value structure and reliability."
},

{
symbol:"⚡",
title:"The Catalyst",
desc:"People who stimulate change when environments become stagnant."
},

{
symbol:"👁",
title:"The Observer",
desc:"Observers who notice patterns and underlying meanings."
},

{
symbol:"♟",
title:"The Analyst",
desc:"Analytical thinkers who evaluate situations before acting."
},

{
symbol:"⚔",
title:"The Initiator",
desc:"People who naturally begin actions or movements."
},

{
symbol:"🧭",
title:"The Explorer",
desc:"Explorers driven by curiosity and discovery."
},

{
symbol:"⚖",
title:"The Mediator",
desc:"Balancers who restore harmony between perspectives."
},

{
symbol:"✧",
title:"The Visionary",
desc:"Future-oriented thinkers who imagine possibilities."
},

{
symbol:"♛",
title:"The Sovereign",
desc:"Stabilizing leaders who organize environments through responsibility."
}

]


// ==============================
// STATE
// ==============================

let index = 0


// ==============================
// UPDATE FUNCTION
// ==============================

function updateSlide(){

    const titleEl = document.getElementById("archetype-title")
    const descEl = document.getElementById("archetype-desc")
    const symbolEl = document.getElementById("archetype-symbol")

    // safety (prevents crash on other pages)
    if(!titleEl || !descEl || !symbolEl) return

    // fade out
    symbolEl.style.opacity = 0
    titleEl.style.opacity = 0
    descEl.style.opacity = 0

    setTimeout(() => {

        // update content
        titleEl.innerText = archetypes[index].title
        descEl.innerText = archetypes[index].desc
        symbolEl.innerText = archetypes[index].symbol

        // re-trigger animation (IMPORTANT)
        symbolEl.style.animation = "none"
        symbolEl.offsetHeight // force reflow
        symbolEl.style.animation = ""

        // fade in
        symbolEl.style.opacity = 1
        titleEl.style.opacity = 1
        descEl.style.opacity = 1

    }, 180)
}


// ==============================
// NAVIGATION
// ==============================

function nextArchetype(){

    index++
    if(index >= archetypes.length){ index = 0 }

    updateSlide()
}

function prevArchetype(){

    index--
    if(index < 0){ index = archetypes.length - 1 }

    updateSlide()
}


// ==============================
// INIT ON LOAD
// ==============================

window.addEventListener("DOMContentLoaded", () => {
    updateSlide()
})