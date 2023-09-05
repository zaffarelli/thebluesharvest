
class Frontdoor{
    constructor(){
        let me = this;
    }

    registerPictures(){
        console.log("Register pictures");
        $('.picture').off('click').on('click', function(e){
            e.preventDefault();
            e.stopPropagation();
           $('#overlay').removeClass('hidden');
           let picture_ref = $(this).attr('ref');
           console.log(picture_ref);
           $(".popin").html("<img src='"+picture_ref+"'>");



        });
        $('#overlay').off('click').on('click', function(e){
            e.preventDefault();
            e.stopPropagation();
           $('#overlay').addClass('hidden');
           $("#popin").html();

        });
    }


    register(){
        let me = this;
        me.registerPictures();
        console.log("Register");
    }

    perform(){
        let me=this;
        me.register();
        console.log("Perform");
    }

}