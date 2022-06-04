console.log("Hello Memories")

const tofollowmodal = document.getElementById("follow-modal")
const spinnerbox = document.getElementById("spinner-box")

console.log(tofollowmodal)
console.log(spinnerbox)

$.ajax({
    type:"GET",
    url:'/profile/myprofjson/',
    success: function(response){
        const pfdata= response.prof_data
        console.log(pfdata)
        setTimeout(()=>{
            spinnerbox.classList.add("not-visible")
            pfdata.forEach(element => {
                tofollowmodal.innerHTML += `
                <div class="row mb-2 align-items-center">
                    <div class="col-2">
                        <img class="avator" src="${element.avator}" alt="${element.user}" >
                    </div>
                    <div class="col-3">
                    <div class="text-muted">${element.username}</div>
                    </div>
                    <div class="col text-right">
                        <button class="btn btn-success"> Follow</button>
                    </div>
                </div>
                `
            });
        }, 2000 )
    },
    error:function(error){
        console.log(error)
    }

})