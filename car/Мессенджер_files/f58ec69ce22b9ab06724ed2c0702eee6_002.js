﻿(self.webpackChunkvk=self.webpackChunkvk||[]).push([[78204],{667311:(e,t,o)=>{"use strict";o.d(t,{jsonpManager:()=>s,Upload:()=>r});o(446964),o(66108),o(296253),o(21466),o(283946),o(59357),o(751876);var i=o(791563),a=o(917999),n=o(124961),l=o(873078),s={c:1,h:{},reg:function(e){return s.h[s.c]=(0,a.isFunction)(e)?e:function(){},s.c++}},r={init:function(e,t,o,i){window.uploadInterface=void 0!==window.uploadInterface?window.uploadInterface+1:0;var a=window.uploadInterface;return each(["obj","dropbox","options","vars","types","uploadUrls","callbacks","checks","dragTimer"],(function(e,t){r[t]||(r[t]={})})),this.obj[a]=ge(e),i.dropbox&&(this.dropbox[a]=ge(i.dropbox)),this.vars[a]=o,i.file_input=ge(i.file_input),this.options[a]=i,i.clear&&cur.destroy.push(r.deinit.pbind(a)),this.uploadUrls[a]=t,!i.flash_lite||browser.flash||this.checkFileApi()?i.customShowProgress?i.customShowProgress():"INPUT"!==this.obj[a].tagName||this.checkFileApi()?i.flash_lite||(this.obj[a].innerHTML='<div class="upload_check loading">'+getProgressHtml("","pr_medium upload_pr")+"</div>"):this.obj[a]=ge(i.fieldEl)||this.obj[a].parentNode.firstChild:this.obj[a]=ge(i.fieldEl)||this.obj[a].parentNode.firstChild,i.noCheck?this.embed(a):this.check(a),a},deinit:function(e){if(r.obj[e]){var t=(r.options[e]||{}).dragEvObj,o=r.obj[e];if(t&&(removeEvent(t,"dragenter"),removeEvent(t,"dragover"),removeEvent(t,"dragleave")),o.innerHTML="",each(["obj","dropbox","options","vars","types","uploadUrls","callbacks"],(function(t,o){r[o]&&delete r[o][e]})),r.callbacks){var i=["oncheck","ondone","onfail"];each(r.flashCallbacks(),(function(e,t){i.push(e)})),each(i,(function(t,o){delete r.callbacks[o+e]}))}clearTimeout(r.checks["timer"+e]),clearTimeout(r.dragTimer[e]),delete r.dragTimer[e]}},check:function(e){var t=this.obj[e],o=this.vars[e],i=this.options[e],a=i.check_url?i.check_url:this.uploadUrls[e],n={};if(i.signed){if(!a)return r.onCheckComplete(e);extend(n,{_jsonp:s.reg((function(t){r.onCheckComplete(e,t)}))})}else{if(!i.check_hash&&!i.server)return r.onCheckComplete(e);if(i.use_go_uploader)return r.onCheckComplete(e);this.callbacks["oncheck"+e]=r.onCheckComplete.pbind(e);var l=["mid","aid","gid","hash","rhash"];for(var d in l)l.hasOwnProperty(d)&&(n[l[d]]=o[l[d]]);i.check_aid&&(n.aid=i.check_aid),i.check_gid&&(n.gid=i.check_gid),i.check_hash&&(n.hash=i.check_hash),i.check_rhash&&(n.rhash=i.check_rhash),o.https_resp&&(n.https_resp=o.https_resp),extend(n,{al:1,act:"check_upload",type:i.type,ondone:"Upload.callbacks.oncheck"+e})}var p='<form action="'+a+'" enctype="multipart/form-data" method="post" id="check_upload_form'+e+'" target="check_iframe'+e+'">';for(var u in n)n.hasOwnProperty(u)&&(p+='<input type="hidden" name="'+u+'" value="'+n[u]+'" />');p+='</form><iframe style="visibility: hidden; width: 1px; height: 1px;" id="check_iframe'+e+'" name="check_iframe'+e+'"></iframe>';var c=ce("div",{id:"check_upload_"+e,innerHTML:p,className:i.checkClass||""},{display:"none"});ge("check_upload_"+e)&&re("check_upload_"+e),t.appendChild(c);var h=ge("check_upload_form"+e);if(h)try{h&&h.submit(),clearTimeout(r.checks["timer"+e]),this.checks["timer"+e]=setTimeout(r.serverFail.pbind(e),1e4)}catch(e){debugLog(e)}},onCheckComplete:function(e,t){clearTimeout(r.checks["timer"+e]),delete r.checks["timer"+e];var o={},i=r.options[e],a=t;if(i.signed)o=parseJSON(t||"{}");else{for(var n in t=(t=t||"").split("&"))if(t.hasOwnProperty(n)){var l=t[n].split("=");o[l[0]]=l[1]}a=o}i.customHideProgress&&i.customHideProgress(),o.error||o.fail?r.serverFail(e,a):(i.noCheck=1,i.onCheckComplete?i.onCheckComplete(e):i.flash_lite&&browser.flash?r.initFlash(e,r.obj[e]):r.embed(e),r.serverSuccess(e,a))},serverFail:function(e,t){var o=r.obj[e],a=r.options[e],n=r.vars[e];if(o&&(a.signed||a.server))if(r.fails||(r.fails={}),r.fails[e]=r.fails[e]?r.fails[e]+1:1,a.signed){var l=r.uploadUrls[e].split("?"),s=AjaxConvert.fromQueryString(l[1]),d=extend({act:"check_result",_resign:s._query||l[1]},t?{_query:t}:{_check:a.check_url.split("?")[1]});ajax.post("upload_fails.php",d,{onDone:function(t,n,l,s){r.fails[e]<a.max_attempts?(r.uploadUrls[e]=t,extend(r.options[e],{check_url:n,base_url:l,static_url:s}),r.check(e)):(o.innerHTML="",a.lang&&a.lang.cannot_upload_title&&a.lang.cannot_upload_text&&(0,i.showFastBox)({title:a.lang.cannot_upload_title,width:430,dark:1,bodyStyle:"padding: 20px; line-height: 160%;"},a.lang.cannot_upload_text))}})}else{var p=extend({act:"fail",role:a.type,mid:n.mid,oid:n.oid,gid:n.gid,aid:n.aid,server:a.server,st2_server:a.st2_server,error:a.error,hash:a.error_hash,hash_extra:n.hash_extra},t);a.custom_hash&&extend(p,{custom_hash:a.custom_hash,photo_hash:n.photo_hash,size:n.size,fid:n.fid,vid:n.vid,tag:n.tag}),n.transform_entry&&extend(p,{transform_entry:n.transform_entry,transform_hash:n.transform_hash,security_hash:n.security_hash}),ajax.post("upload_fails.php",p,{onDone:function(t,n,l){r.fails[e]<a.max_attempts?(r.uploadUrls[e]=t,extend(r.options[e],l),extend(r.vars[e],n),r.check(e)):(o.innerHTML="",a.lang&&a.lang.cannot_upload_title&&a.lang.cannot_upload_text&&(0,i.showFastBox)({title:a.lang.cannot_upload_title,width:430,dark:1,bodyStyle:"padding: 20px; line-height: 160%;"},a.lang.cannot_upload_text))}})}},serverSuccess:function(e,t){var o=r.options[e],i=r.vars[e];if(r.checked=r.checked||{},r.checked[e]=1,o.signed)ajax.post("upload_fails.php",{act:"check_result",_query:t});else if(o.server||o.error_hash){var a=extend({act:"success",mid:i.mid,oid:i.oid,gid:i.gid,aid:i.aid,server:o.server,error:o.error,hash:o.error_hash},t);ajax.post("upload_fails.php",a)}},embed:function(e){var t=null!=e.num?e.num:e,o=this.obj[t],i=this.dropbox[t],a=this.options[t];a.noEmbed?re("check_upload_"+e):a.noCheck&&(browser.flash>9&&a.forceFlash?this.initFlash(t,o):this.checkFileApi()&&!a.flash_lite?this.initFileApi(t,o,i):browser.flash>9&&!a.noFlash?this.initFlash(t,o):a.noForm||this.initForm(t,o))},checkFileApi:function(){return(window.XMLHttpRequest||window.XDomainRequest)&&(window.FormData||window.FileReader&&(window.XMLHttpRequest&&XMLHttpRequest.sendAsBinary||window.ArrayBuffer&&window.Uint8Array&&(window.MozBlobBuilder||window.WebKitBlobBuilder||window.BlobBuilder)))},initFlash:function(e,t){var o=[],i=r.vars[e],a=r.options[e],n={url:a.flashPath||"/swf/uploader_lite.swf",id:"uploader_lite"+e,preventhide:!0,width:"100%",height:browser.safari||browser.msie||browser.chrome&&intval(browser.version)<17?a.flashHeight?a.flashHeight+"px":cur.flash_lite&&!isVisible("photos_flash_add_button")?"67px":"25px":"100%"},l={swliveconnect:"true",allowscriptaccess:"always",wmode:browser.msie?"opaque":"transparent"};for(var s in r.types[e]="flash",i)i.hasOwnProperty(s)&&o.push(s+"="+i[s]);a.signed||i.ajx||o.push("ajx=1");var d=this.flashCallbacks(),p={};this.callbacks=this.callbacks||{},each(d,(function(t,o){r.callbacks[t+e]=o.pbind(e),p[t]="Upload.callbacks."+t+e}));var u=clone(i);if(extend(u,p,{upload_url:r.uploadUrls[e],file_size_limit:a.file_size_limit,file_types_description:a.file_types_description,file_types:a.file_types,file_name:a.file_name,post_data:escape(o.join("&"))}),a.flash_lite?t.innerHTML='<div class="lite_upload" id="lite_upload'+e+'" style="z-index:10000; width: 100%; height: 100%; cursor: pointer;"></div>':(a.lang.button_browse||(a.lang.button_browse="Выбрать файл"),a.flat_button?t.innerHTML='<div id="uploader'+e+'" style="position: relative;"><div id="lite_upload'+e+'" style="position: absolute; height: 100%; width: 100%; z-index: 10000; cursor: pointer;"></div><button class="flat_button button_big button_big_width">'+a.lang.button_browse+"</button></div>":t.innerHTML='<button id="uploader'+e+'" class="flat_button upload_btn '+(a.buttonClass||"")+'" style="position: relative;"><div id="lite_upload'+e+'" style="position: absolute; height: 100%; width: 100%; z-index: 10000; cursor: pointer;"></div>'+a.lang.button_browse+"</button>"),renderFlash(ge("lite_upload"+e),n,l,u),browser.msie&&setStyle(ge("lite_upload"+e),{opacity:0,cursor:"pointer"}),a.lang.switch_mode){var c=a.lang.switch_mode.replace("{link}",'<a onclick="Upload.switchMode('+e+');">');c=c.replace("{/link}","</a>"),t.appendChild(ce("div",{innerHTML:c,align:"left",className:"upload_switch_mode"},{marginTop:"15px"}))}},initForm:function(e,t){var o=e,i=this.vars[o],a=this.options[o];this.types[o]="form";var n='<form action="'+this.uploadUrls[o]+'" enctype="multipart/form-data" method="post" id="file_uploader_form'+o+'" target="upload_iframe'+o+'" style="text-align: center; width: 100%;">';if(a.signed)extend(i,{_jsonp:s.reg((function(e){r.onUploadComplete(o,e)}))});else{var l=r.onUploadComplete.pbind(o),d=r.onUploadError.pbind(o);this.callbacks["ondone"+o]=function(){var e=l.pbind.apply(l,arguments);setTimeout((function(){e()}),1)},this.callbacks["onfail"+o]=function(){var e=d.pbind.apply(d,arguments);setTimeout((function(){e()}),1)},extend(i,{al:1,ondone:"Upload.callbacks.ondone"+o,onfail:"Upload.callbacks.onfail"+o})}for(var p in i)i.hasOwnProperty(p)&&(n+='<input type="hidden" name="'+p+'" value="'+i[p]+'" />');var u='<input type="file" class="file" size="28" onchange="'+(a.uploadButton?"Upload.onUploadFileSelected("+o+")":"Upload.onUploadStart("+o+");")+'" name="'+a.file_name+'" style="cursor: pointer;"'+(a.accept?' accept="'+a.accept+'"':"")+'/></form><iframe style="position: absolute; visibility: hidden; width: 1px; height: 1px;" id="upload_iframe'+o+'" name="upload_iframe'+o+'"></iframe>';a.label?n+=a.label.split("{file}").join(u):n+=u,t.innerHTML=n;var c=a.file_input,h=geByClass1("file",t,"input");delete a.file_input,c&&h&&(h.parentNode.replaceChild(c,h),c.onchange=function(){r.onUploadStart(o)},window.data(c,"changed")&&(window.data(c,"changed",!1),c.onchange())),a.uploadButton&&a.setUploadAction?a.setUploadAction(e,(function(){r.onUploadStart(o)})):a.uploadButton&&!0!==a.uploadButton&&(ge(a.uploadButton).onclick=function(){r.onUploadStart(o)})},buttonOver:function(e){var t=r.options[e];t.flash_lite?t.hoverEl?addClass(t.hoverEl,"hover"):isVisible("photos_flash_add_button")?addClass(ge("photos_flash_add_button"),"hover"):addClass(ge("photos_upload_area"),"hover"):addClass(ge("lite_upload"+e).nextSibling,"hover")},buttonOut:function(e){var t=r.options[e];t.flash_lite?t.hoverEl?removeClass(t.hoverEl,"hover"):isVisible("photos_flash_add_button")?(removeClass(ge("photos_flash_add_button"),"hover"),removeClass(ge("photos_flash_add_button"),"active")):removeClass(ge("photos_upload_area"),"hover"):(removeClass(ge("lite_upload"+e).nextSibling,"hover"),removeClass(ge("lite_upload"+e).nextSibling,"active"))},buttonDown:function(e){r.options[e].flash_lite?isVisible("photos_flash_add_button")&&addClass(ge("photos_flash_add_button"),"active"):addClass(ge("lite_upload"+e).nextSibling,"active")},buttonUp:function(e){r.options[e].flash_lite?isVisible("photos_flash_add_button")&&removeClass(ge("photos_flash_add_button"),"active"):removeClass(ge("lite_upload"+e).nextSibling,"active")},initFileApi:function(e,t,o){var i,a=this.options[e],n=a&&a.dragEl||window.boxLayerWrap;if(o&&n&&(r.addedDocEvent||(addEvent(document,"drop",r.drop),r.addedDocEvent=!0),a.dragEvObj=n,addEvent(n,"dragenter",r.dragEnter.pbind(e)),addEvent(n,"dragover",r.dragOver.pbind(e)),addEvent(n,"dragleave",r.dragOut.pbind(e))),this.types[e]="fileApi",a.chooseBox)i='<input class="file" type="file" size="28" onchange="Upload.onFileApiSend('+e+', this.files);"'+(a.multiple?' multiple="true"':"")+(a.accept?' accept="'+a.accept+'"':"")+' name="'+a.file_name+'" style="cursor: pointer;"/>';else if(a.uploadButton)a.lang.button_browse||(a.lang.button_browse="Выбрать файл"),i='<button class="flat_button upload_btn fl_l '+(a.buttonClass||"")+'" onclick="this.nextSibling.nextSibling.click()">'+a.lang.button_browse+'</button><div class="upload_selected fl_l" style="padding: 4px 0 0 10px;"></div><input class="file" type="file" size="28" onchange="geByClass1(\'upload_selected\', this.parentNode).innerHTML = Upload.getFilesNames('+e+", this.files); Upload.onUploadFileSelected("+e+')"'+(a.multiple?' multiple="true"':"")+(a.accept?' accept="'+a.accept+'"':"")+' name="'+a.file_name+'" style="visibility: hidden; position: absolute;"/><br class="clear" />';else if(a.lang.button_browse||(a.lang.button_browse="Выбрать файл"),a.flat_button){var s=l.FlatButton.render({className:"upload_btn"+(a.buttonClass||""),appearance:l.FlatButtonAppearance.PRIMARY,size:l.FlatButtonSize.M,children:a.lang.button_browse,restAttrs:{onclick:"document.querySelector('.flat_button_file').click()"}}),d=`<input class="file flat_button_file" type="file" size="28"\n                     onchange="Upload.onFileApiSend('${e}', this.files);" ${a.multiple?' multiple="true"':""} ${a.accept?' accept="'+a.accept+'"':""} name="${a.file_name}" style="visibility: hidden; position: absolute;"/>\n                `,p=document.createElement("div");p.appendChild(s),p.insertAdjacentHTML("beforeend",d),i=p.innerHTML}else i='<button class="flat_button upload_btn '+(a.buttonClass||"")+'" onclick="this.nextSibling.click()">'+a.lang.button_browse+'</button><input class="file" type="file" size="28" onchange="Upload.onFileApiSend('+e+', this.files);"'+(a.multiple?' multiple="true"':"")+(a.accept?' accept="'+a.accept+'"':"")+' name="'+a.file_name+'" style="visibility: hidden; position: absolute;"/>';a.label&&!a.flat_button?t.innerHTML=a.label.split("{file}").join(i):t.innerHTML=i;var u=a.file_input,c=geByClass1("file",t,"input");u&&c&&(c.parentNode.replaceChild(u,c),u.onchange=function(){r.onFileApiSend(e,this.files)},window.data(u,"changed")&&(window.data(u,"changed",!1),setTimeout(u.onchange.bind(u),0))),a.uploadButton&&a.setUploadAction?a.setUploadAction(e,(function(){r.onFileApiSend(e,geByTag1("input",t).files)})):a.uploadButton&&!0!==a.uploadButton&&(ge(a.uploadButton).onclick=function(){r.onFileApiSend(e,geByTag1("input",t).files)})},switchMode:function(e){r.options[e].noFlash=r.options[e].noCheck=1,r.embed(e)},onUploadFileSelected:function(e){r.options[e].onUploadFileSelected&&r.options[e].onUploadFileSelected()},onUploadStart:function(e,t){cur.fileApiUploadStarted=!0;var o=void 0!==e.ind?e.ind:e;"form"==r.types[o]&&(ge("file_uploader_form"+o).submit(),geByClass1("file",r.obj[o]).disabled=!0);var i=r.options[o];i.onUploadStart&&i.onUploadStart(e,t)},getErrorAdditional:function(e){return e.error&&void 0!==e.server&&void 0!==e.bwact?(-1!==e.error.indexOf(":")?",":":")+" from upl_"+intval(e.server)+"?act="+e.bwact.replace(/[^a-zA-Z_0-9]/g,""):""},onUploadComplete:function(e,t,o){var i,a=void 0!==e.ind?e.ind:e,n=r.options[a];(void 0!==o&&a===e&&(e=o),"object"==typeof e&&(e.ind=a),"form"==r.types[a])&&(geByClass1("file",r.obj[a]).disabled=!1);if(n.onUploadComplete){var l="";n.signed&&((i=t?parseJSON(t):"")?l=r.getErrorAdditional(i):t='{"error":"ERR_CLIENT_UPLOAD_FAIL: upload request bad result, url \\"'+r.uploadUrls[a]+'\\""}'),n.onUploadComplete(e,t,l)}"form"==r.types[a]&&r.onUploadCompleteAll(e,t),"video"===n.type?statlogsValueEvent("upload_video_fails",1,n.server,"success"):"photo"===n.type?statlogsValueEvent("upload_photo_fails",1,n.server,"success"):"doc"===n.type&&statlogsValueEvent("upload_doc_fails",1,n.server,"success")},onUploadCompleteAll:function(e,t,o){var i=void 0!==e.ind?e.ind:e,a=r.options[i];if(void 0!==o&&i===e&&(e=o),"fileApi"===r.types[i]){var n=geByClass1("file",r.obj[i],"input");n&&(n.value="")}var l={duration:Date.now()-a.uploadStartedTs,type:a.type,total_size:a.filesTotalSize};"subtitles"!==a.type&&this.sendUploadStat(i,l),a.onUploadCompleteAll&&a.onUploadCompleteAll(e,t)},onUploadError:function(e,t){var o=void 0!==e.ind?e.ind:e,i=r.options[o];"form"===r.types[o]&&(geByClass1("file",r.obj[o]).disabled=!1);i.signed?i.onUploadComplete&&i.onUploadComplete(e,'{"error":"ERR_CLIENT_UPLOAD_FAIL: upload request fail, code \\"'+t.replace(/([\\\"])/g,"\\$1").replace(/\n/g,"\\n")+'\\", url \\"'+r.uploadUrls[o]+'\\""}'):i.onUploadError&&i.onUploadError(e,t)},onConnectionLost:function(e){var t=void 0!==e.ind?e.ind:e,o=r.options[t];o.onConnectionLost&&o.onConnectionLost(e)},onUploadProgress:function(e,t,o){var i=void 0!==e.ind?e.ind:e,a=r.options[i];a.onUploadProgress&&a.onUploadProgress(e,t,o)},onDebug:function(e,t){var o=void 0!==e.ind?e.ind:e,i=r.options[o];i.onDebug&&i.onDebug(e,t)},onSelectClick:function(e,t){var o=void 0!==e.ind?e.ind:e,i=r.options[o];i.onSelectClick&&i.onSelectClick(e,t)},getFilesNames:function(e,t){if(t&&t.length){var o=this.options[e];return o.multiple?(o.lang.selected_num_files||(o.lang.selected_num_files=["","%s файл","%s файла","%s файлов"]),langNumeric(t.length,o.lang.selected_num_files)):t[0].name.replace(/[&<>"']/g,"")}},checkFileType:function(e,t,o){var i=!1;if(o&&""!==o){var a=!0;if(each(o.split(";"),(function(t,o){if(o=o.substr(1).toLowerCase(),e.substr(-o.length).toLowerCase()==o)return a=!1,!1})),!a)return!1}return each(t.split(";"),(function(t,o){if(o=o.substr(1).toLowerCase(),e.substr(-o.length).toLowerCase()==o||".*"==o)return i=!0,!1})),i},checkFilesSizes:function(e,t){var o=this.options[e];if(o.file_size_limit)for(var a in t)if(t.hasOwnProperty(a)){var n=t[a];if(n.size&&n.size>o.file_size_limit){var l=o.lang.filesize_error;return l&&l.indexOf("{count}")>=0&&(l=o.file_size_limit>=1048576?l.replace("{count}",intval(o.file_size_limit/1048576)):l.replace("{count}",intval(o.file_size_limit/1024))),l&&(0,i.showFastBox)({title:getLang("global_error"),width:430,dark:1,bodyStyle:"padding: 20px; line-height: 160%;",onHide:function(){r.embed(e),delete cur.notStarted}},l,getLang("global_cancel")),!1}}return!0},onFileApiSend:function(e,t,o){if(t&&t.length){var a=this.options[e];if(a.file_types){var n=[];if(each(t,(function(e,t){r.checkFileType(t.name,a.file_types,a.file_disallowed_types)&&n.push(t)})),!n.length)return void(a.onNoFilteredCallback&&a.onNoFilteredCallback(t));t=n}if((!a.filterCallback||(t=a.filterCallback(e,t)).length)&&(a.reverse_files&&(t=Array.prototype.slice.call(t).reverse()),!a.multiple&&t.length>1&&(t=[t[0]]),this.checkFilesSizes(e,t))){if(a.photoBox&&!o)return r.onPhotoAdd(e,t);if(!a.withoutAutoUpload||o){a.beforeUpload&&a.beforeUpload(e),cur.notStarted=cur.fileApiUploadStarted=!0,a.multi_progress||this.onUploadStart({ind:e,fileName:(t[0].fileName||t[0].name||"").replace(/[&<>"']/g,"")});var l=t.length;if(a.max_files){var s=cur.attachCount;if(!s&&cur.addMedia){var d=-1;for(var p in cur.addMedia)p>d&&(d=p);d>=0&&cur.addMedia[d]&&cur.addMedia[d].attachCount&&(s=cur.addMedia[d].attachCount)}var u=s?s():0,c=(a.max_files_warning||getLang("global_attach_max_n_files",a.max_files)).replace("{count}",a.max_files);a.max_files-u<t.length?(l=a.max_files-u,(0,i.showFastBox)({title:getLang("global_error"),width:430,dark:1,bodyStyle:"padding: 20px; line-height: 160%;",onHide:function(){r.embed(e),delete cur.notStarted,a.onMaxCount&&a.onMaxCount()}},c,getLang("global_continue"),(function(){r.uploadFiles(e,t,l),a.max_files_hide_last?curBox().hide():boxQueue.hideAll()}),getLang("global_cancel"))):(a.force_max_files&&(l=Math.min(l,a.max_files-(cur.savedPhotos||[]).length)),this.uploadFiles(e,t,l))}else this.uploadFiles(e,t,l)}else a.onFilesSelected&&a.onFilesSelected(e,t)}}},onPhotoAdd:function(e,t){var o=0,i=0;r.fileList=r.fileList||{},r.fileList[e]||(r.fileList[e]=[],r.options[e].onPhotoBox&&(o=!0)),each(t,(function(t,o){i++;var a=r.options[e].photoBox,n=new RegExp("image.*");o.type.match(n),cur.uploaderPhotoId=(cur.uploaderPhotoId||0)+1;var l=cur.uploaderPhotoId;r.fileList[e][l]=o;var s=ce("img"),d=ce("div",{id:"photos_add_item"+l,className:"photos_add_item",innerHTML:'<span class="photos_add_img photos_add_wait" id="photos_add_cont'+l+'" onmouseover="PhotosAdd.thumbOver('+l+', this);" onmouseout="PhotosAdd.thumbOut('+l+');"><span class="photos_add_s" id="photos_add_s'+l+'">&nbsp;</span></span><span class="bg">&nbsp;</span>'});a.appendChild(d);var p=new FileReader;p.onload=function(e){s.src=e.target.result,s.onload=function(){s.onload=!1;var e,t,o={w:s.width,h:s.height};o.w>130&&(e=130/o.w,o.w=130,o.h=parseInt(o.h*e)),o.h>130&&(t=130/o.h,o.h=130,o.w=parseInt(o.w*t));var i=ce("canvas",{width:o.w,height:o.h});i.getContext("2d").drawImage(s,0,0,o.w,o.h);var a=i.toDataURL("image/jpeg");s.src=a;var n=ge("photos_add_s"+l),d=Math.max(o.w,80),p=Math.min(o.h,98);setStyle(n,{width:d,height:p,marginLeft:Math.ceil((130-d)/2)}),n.innerHTML="",n.appendChild(s),s.onload=function(){setTimeout((function(){n.parentNode.className="photos_add_img"}),0),s.onload=!1},r.finishTask()}},r.taskToQ((function(){p.readAsDataURL(o)}))})),o&&i&&r.options[e].onPhotoBox(),r.options[e].onPhotoAdd&&i&&r.options[e].onPhotoAdd()},uploadPhotos:function(e){var t=[],o=r.fileList[e];for(var i in o)o[i]&&t.push(extend(o[i],{fileRef:i}));return r.options[e].onUploadStart&&r.options[e].onUploadStart(),!!t.length&&(cur.uploadCount=Math.min(500,t.length),r.uploadFiles(e,t,cur.uploadCount),!0)},taskToQ:function(e){if(r.previewFileQ||(r.previewFileQ=[]),e&&r.previewFileQ.push(e),!r.doingQ){var t=r.previewFileQ.shift();t&&(r.doingQ=!0,t())}},finishTask:function(){setTimeout((function(){r.doingQ=!1,r.taskToQ()}),100)},uploadFiles:function(e,t,o){if(!(o<=0)){var i,a=this.options[e],n=a.signed?this.vars[e]:extend(this.vars[e],{ajx:1}),l=0,s=0,d=0,p=0,u=[];a.uploading&&(l=a.filesTotalSize||0,s=a.filesTotalCount||0,p=a.filesLoadedCount||0,d=a.filesLoadedSize||0,u=a.filesQueue),a.file_match&&(i=new RegExp(a.file_match,"i"));for(var c=!1,h=0;h<o;h++){var f=(t[h].fileName||t[h].name||"").replace(/[&<>"']/g,"");!a.file_match||f.match(i)?(a.multi_progress&&!a.multi_sequence&&this.onUploadStart({ind:e,fileName:f}),l+=t[h].size,s+=1,u.push(t[h])):c=!0}if(u.reverse(),extend(a,{filesQueue:u,filesTotalSize:l,filesLoadedSize:d,filesLoadedCount:p,filesTotalCount:s,uploadStartedTs:Date.now()}),u.length>0)if(void 0!==cur.multiProgressIndex)cur.nextQueues||(cur.nextQueues=[]),cur.nextQueues.push(e);else{var g=AjaxConvert.toQueryString(n),m=this.uploadUrls[e]?this.uploadUrls[e]+(this.uploadUrls[e].match(/\?/)?"&":"?")+g:"";a.use_go_uploader&&(m=this.uploadUrls[e]),this.uploadFile(e,u.pop(),m),a.multi_progress&&(cur.multiProgressIndex=e)}else c&&r.onUploadError(e,"file type not supported")}},getFileInfo:function(e,t,o){return t.multi_progress?{ind:e,fileName:o?(o.fileName||o.name||"").replace(/[&<>"']/g,""):"",num:t.filesLoadedCount,totalSize:t.filesTotalSize,loadedSize:t.filesLoadedSize,totalCount:t.filesTotalCount,file:o}:e},supportsChunkedUpload:function(){return!!Blob&&!!(Blob.prototype.webkitSlice||Blob.prototype.mozSlice||Blob.prototype.slice)&&!!FileReader},uploadFileChunked:function(e,t,o){var i=this.options[e],a=r.getFileInfo(e,i,t);i.multi_sequence&&this.onUploadStart(a);var n={file:t,fileName:(t.name||t.fileName).replace(/[&<>"']/g,""),fileSize:t.size,fileMime:t.type,retryCount:0,timeouts:[],activeRequests:[],requestsProgress:{},pointer:0,isUvUpload:Boolean(this.isUvUpload||i.isUvUpload),state:{url:o,started:Date.now(),loaded:null,chunkSize:i.chunkSize||4194304,sessionId:(1e17*Math.random()).toString(16)}};n.abort=function(e){each(e.timeouts,(function(e,t){clearTimeout(t)})),each(e.activeRequests,(function(e,t){t.abort()})),e.timeouts=[],e.activeRequests=[]}.bind(null,n),n.chunksNum=Math.ceil(n.fileSize/n.state.chunkSize),n.chunksLeft=n.chunksNum;var l=function(e){n.storageKey=["upload",e,n.fileSize].join("_"),i.uploading=!0,i.chunkedUpload=n;var t=ls.get(n.storageKey);t&&(Date.now()-t.started<864e5?(n.state=t,o=t.url):ls.remove(n.storageKey));try{console.log("%c Warning: if devtools is logging network requests it may cause high memory usage during file upload","font-size:16px;color:orange;")}catch(e){}p()};if(i.isUvUpload){var s=r.vars[e];ajax.post("al_video.php?act=get_upload_url",{file_size:t.size?t.size:0,user_agent:window.navigator.userAgent,owner_id:s.oid,tag:s.tag,from:s.from,extra_upload_options:i.extraUploadOptions},{onDone:function(s){n.state.url=s.upload_url,o=n.state.url,r.uploadUrls[e]=o,d(t,l),i.onUploadedVideoIdReceived&&i.onUploadedVideoIdReceived(a,s.video_id)},onFail:function(){r.terminateUpload(e,t.name)}})}else d(t,l);function d(e,t){var o=1048576,i=Math.floor(e.size/2)-524288,a=[e.slice(0,o),e.slice(i,i+o),e.slice(e.size-o,e.size)];!function e(o){var i=a.shift();if(i){var n=new FileReader;n.addEventListener("loadend",(function(t){var i=new Uint8Array(t.target.result),a=function(){var e=65535,t=65535;return{append:o,result:i};function o(o){for(var i=o.length,a=0;i;){var n=i>359?359:i;i-=n;do{t+=e+=o[a++]}while(--n);e=((65535&e)>>>0)+(e>>>16),t=((65535&t)>>>0)+(t>>>16)}}function i(){return((t=((65535&t)>>>0)+(t>>>16))<<16>>>0|(e=((65535&e)>>>0)+(e>>>16)))>>>0}}();a.append(i),o+=a.result().toString(16),e(o)})),n.readAsArrayBuffer(i)}else t(o)}("")}function p(){for(n.pointer=0,n.chunksLeft=n.chunksNum;n.activeRequests.length<4&&n.pointer<n.fileSize;)u()}function u(){var e=n.pointer,t=Math.min(e+n.state.chunkSize,n.fileSize)-1;if(!(e>=n.fileSize)){var o=!1;n.state.loaded&&each(n.state.loaded.split(","),(function(i,a){var l=a.match(/^(\d+)-(\d+)\/\d+$/),s=parseInt(l[1]),r=parseInt(l[2]);if(e>=s&&t<=r)return o=!0,n.chunksLeft-=Math.ceil((r+1-e)/n.state.chunkSize),n.pointer=r+1,!1})),o?(h(),u()):(c(e,t),n.pointer+=n.state.chunkSize)}}function c(l,s){var d=(t.slice||t.webkitSlice||t.mozSlice).call(t,l,s+1),g=new XMLHttpRequest;g.open("POST",o,!0),g.upload.onprogress=function(e){g.readyState!==XMLHttpRequest.DONE&&(e.lengthComputable&&(n.requestsProgress[l]=e.loaded),h())},g.onload=function(d){var c;n.activeRequests.splice(indexOf(n.activeRequests,d.target),1),n.retryCount=0,--n.chunksLeft,201==d.target.status?(n.chunksLeft?(n.state.loaded=d.target.responseText,ls.set(n.storageKey,n.state),u()):(n.state.loaded=d.target.responseText,ls.set(n.storageKey,n.state),p()),delete n.requestsProgress[l],h()):200==d.target.status?(ls.remove(n.storageKey),c=d.target.responseText,extend(a,r.getFileInfo(e,i,t)),r.options[e].filesLoadedSize+=n.fileSize,r.options[e].filesLoadedCount+=1,r.onUploadComplete(a,c),r.options[e].filesQueue&&r.options[e].filesQueue.length>0?r.uploadFile(e,r.options[e].filesQueue.pop(),o):(r.startNextQueue(e),r.onUploadCompleteAll(a,c),i.uploading=!1)):(ls.remove(n.storageKey),n.abort(),r.onUploadError(a),r.options[e].filesQueue.length||(r.startNextQueue(e),r.onUploadCompleteAll(a,d.target.responseText),i.uploading=!1),f(d.target.status,d.target.responseText,l+"-"+s))},g.onerror=function(e){if(n.activeRequests.splice(indexOf(n.activeRequests,e.target),1),++n.retryCount<=50){var t=setTimeout(c.bind(null,l,s),300*n.retryCount);n.timeouts.push(t)}else n.abort(),r.onConnectionLost(a);h(),f(e.target.status,e.target.responseText,l+"-"+s)},n.isUvUpload&&g.setRequestHeader("X-Uploading-Mode","parallel"),g.setRequestHeader("Content-Disposition",'attachment, filename="'+encodeURI(n.fileName)+'"'),g.setRequestHeader("Content-Type",n.fileMime||"application/octet-stream"),g.setRequestHeader("Content-Range","bytes "+l+"-"+s+"/"+n.fileSize),g.setRequestHeader("Session-ID",n.state.sessionId),g.send(d),d=null,n.activeRequests.push(g)}function h(){var o=n.fileSize,l=(n.chunksNum-n.chunksLeft)*n.state.chunkSize;each(n.requestsProgress,(function(e,t){l+=t})),extend(a,r.getFileInfo(e,i,t)),i.multi_progress?r.onUploadProgress(a,l,o):r.onUploadProgress(e,Math.min(l+i.filesLoadedSize,i.filesTotalSize),i.filesTotalSize)}function f(e,t,i){ajax.post("al_video.php",{act:"uploadVideoFailStat",url:o,error:e+","+t,range:i,sessionId:n.state.sessionId,chunksLeft:n.chunksLeft,loaded:n.state.loaded})}},resumeUpload:function(e){var t=this.options[e].chunkedUpload;r.uploadFileChunked(e,t.file,t.state.url)},isNeedRequestUrl:function(e){var t=this.options[e];return t.requestOptionsForFile&&"video"===t.type},getUploadOptions:function(e,t){var o=this.options[e],i=cur.gid||0;cur.oid<0&&inArray(cur.module,["public","groups","ads"])&&inArray(o.from,["article","post","ads"])&&(i=-cur.oid),r.options[e].uploadOptionsXhr=ajax.post("al_video.php?act=get_upload_params",{gid:i,from:o.from},{onDone:function(o){var i=AjaxConvert.toQueryString(o.vars),a=o.options.url+(o.options.url.match(/\?/)?"&":"?")+i;extend(r.options[e],o.options),extend(r.vars[e],o.vars),r.uploadUrls[e]=a,r.check(e),r.uploadFile(e,t,a,!0)},onFail:function(){r.terminateUpload(e,t.name)}})},uploadFile:function(e,t,o,i){var a=this.options[e];if(!r.isNeedRequestUrl(e)||i)if(a.chunked&&r.supportsChunkedUpload()&&(Boolean(a.isUvUpload)||t.size>4194304))r.uploadFileChunked.apply(r,arguments);else{var l=browser.msie&&intval(browser.version)<10?window.XDomainRequest:window.XMLHttpRequest,s=r.getFileInfo(e,a,t);a.multi_sequence&&this.onUploadStart(s),a.uploading=!0;var d=null;if(window.FormData){var p=new FormData;t instanceof File?p.append(a.file_name,t):p.append(a.file_name,t,t.filename.replace(/[&<>"']/g,"")),d=new l;d.open("POST",o,!0),d.onload=function(i){extend(s,r.getFileInfo(e,a,t)),r.options[e].filesLoadedSize+=t.size,r.options[e].filesLoadedCount+=1,r.onUploadComplete(s,i.target.responseText),r.options[e].filesQueue&&r.options[e].filesQueue.length>0?r.uploadFile(e,r.options[e].filesQueue.pop(),o):(r.startNextQueue(e),r.onUploadCompleteAll(s,i.target.responseText),a.uploading=!1)},d.onerror=function(i){extend(s,r.getFileInfo(e,a,t)),r.options[e].filesTotalSize-=t.size,r.options[e].filesTotalCount-=1,r.onUploadError(s,i.target.responseText),r.options[e].filesQueue.length>0?r.uploadFile(e,r.options[e].filesQueue.pop(),o):(r.startNextQueue(e),r.onUploadCompleteAll(s,i.target.responseText),a.uploading=!1)},d.upload.onprogress=function(o){d.readyState!==XMLHttpRequest.DONE&&(!1,extend(s,r.getFileInfo(e,a,t)),o.lengthComputable&&(a.multi_progress?r.onUploadProgress(s,o.loaded,o.total):r.onUploadProgress(e,Math.min(o.loaded+a.filesLoadedSize,a.filesTotalSize),a.filesTotalSize)))},d.send(p)}else{(0,n.saveStatlogEvents)({name:"upload_tmp_stat",value:1,keys:["window_formdata_not_exists"]});try{if(l&&!l.prototype.sendAsBinary&&window.ArrayBuffer&&window.Uint8Array){var u=window.MozBlobBuilder||window.WebKitBlobBuilder||window.BlobBuilder;u&&(l.prototype.sendAsBinary=function(e){for(var t=new window.ArrayBuffer(e.length),o=new Uint8Array(t,0),i=0;i<e.length;i++)o[i]=255&e.charCodeAt(i);var a=new u;a.append(t);var n=a.getBlob();this.send(n)})}var c=new FileReader;c.onload=function(){(d=new l).onload=function(i){extend(s,r.getFileInfo(e,a,t)),r.options[e].filesLoadedSize+=t.size,r.options[e].filesLoadedCount+=1,r.onUploadComplete(s,i.target.responseText),r.options[e].filesQueue.length>0?r.uploadFile(e,r.options[e].filesQueue.pop(),o):(r.startNextQueue(e),r.onUploadCompleteAll(s,i.target.responseText))},d.onerror=function(i){extend(s,r.getFileInfo(e,a,t)),r.options[e].filesTotalSize-=t.size,r.options[e].filesTotalCount-=1,r.onUploadError(s,i.target.responseText),r.options[e].filesQueue.length>0?r.uploadFile(e,r.options[e].filesQueue.pop(),o):(r.startNextQueue(e),r.onUploadCompleteAll(s,i.target.responseText),a.uploading=!1)},d.upload.onprogress=function(o){extend(s,r.getFileInfo(e,a,t)),o.lengthComputable&&(a.multi_progress?(r.onUploadProgress(s,o.loaded,o.total),a.uploading=!1):r.onUploadProgress(e,Math.min(o.loaded+a.filesLoadedSize,a.filesTotalSize),a.filesTotalSize))},d.open("POST",o,!0);var i="---------"+irand(1111111111,9999999999);d.setRequestHeader("Content-Type","multipart/form-data, boundary="+i);var n="--"+i+"\r\n";n+="Content-Disposition: form-data; name='"+a.file_name+"'; filename='"+t.name.replace(/[&<>"']/g,"")+"'\r\n",n+="Content-Type: application/octet-stream\r\n\r\n",n+=c.result+"\r\n",n+="--"+i+"--",d.sendAsBinary(n)},c.readAsBinaryString(t)}catch(e){try{console.error(e)}catch(e){}}}r.options[e].xhr=d}else r.getUploadOptions(e,t)},terminateUpload:function(e,t,o){try{var i=r.vars[e],a=r.options[e],n=AjaxConvert.toQueryString(i),l=a.filesQueue,s=!1,d=a.multi_progress?{ind:e,fileName:null==t?void 0:t.replace(/[&<>"']/g,"")}:e,p=t?e+"_"+t:e;for(var u in l)if(t==(l[u].fileName||l[u].name||"").replace(/[&<>"']/g,"")){l.splice(u,1),s=!0;break}o&&o.tt&&o.tt.destroy&&o.tt.destroy(),re("upload"+p+"_progress_wrap"),r.onUploadComplete(d,'{"error":"ERR_UPLOAD_TERMINATED: upload request was terminated"}'),!s&&a.xhr&&a.xhr.abort(),!s&&a.chunkedUpload&&a.chunkedUpload.abort();var c=this.uploadUrls[e]+(this.uploadUrls[e].match(/\?/)?"&":"?")+n;s||(l.length>0?r.uploadFile(e,l.pop(),c):(r.startNextQueue(e),r.onUploadCompleteAll(d,"")))}catch(e){try{console.error(e)}catch(e){}}},terminateAllUploads:function(){this.checked&&each(this.checked,(e=>{if(e=+e,r.isSomethingUploading(e)){var t=r.options[e];if(t){var o="";t.filesQueue&&t.filesQueue.length&&(t.filesQueue=[]),t.xhr&&4!==t.xhr.readyState&&0!==t.xhr.readyState&&(o=t.file_name),t.chunked&&t.chunkedUpload&&t.chunkedUpload.activeRequests.length&&(o=t.chunkedUpload.fileName,this.terminateUpload(e,o)),o&&this.terminateUpload(e,o)}}}))},startNextQueue:function(e){if(void 0===cur.multiProgressIndex&&setTimeout((function(){delete cur.fileApiUploadStarted}),1e3),e==cur.multiProgressIndex)if(this.options[e].multi_progress&&cur.nextQueues&&cur.nextQueues.length){var t=cur.nextQueues[0],o=r.options[t].filesQueue;for(cur.nextQueues.splice(0,1);0==o.length&&cur.nextQueues.length>0;)t=cur.nextQueues[0],cur.nextQueues.splice(0,1),o=r.options[t].filesQueue;if(o.length>0){var i=r.vars[t],a=AjaxConvert.toQueryString(i),n=r.uploadUrls[t]+(r.uploadUrls[t].match(/\?/)?"&":"?")+a;r.uploadFile(t,o.pop(),n),cur.multiProgressIndex=t}else delete cur.multiProgressIndex,setTimeout((function(){delete cur.fileApiUploadStarted}),1e3)}else delete cur.multiProgressIndex,setTimeout((function(){delete cur.fileApiUploadStarted}),1e3)},isFileDrag:function(e){if(!e||e.target&&("IMG"==e.target.tagName||"A"==e.target.tagName))return!1;if(!e.dataTransfer.types)return!0;for(var t=0;t<e.dataTransfer.types.length;t++)if("Files"==e.dataTransfer.types[t])return!0;return!1},dragEnter:function(e,t){cur.uploadDragStarted&&1!=cur.uploadDragStarted||(cur.uploadDragStarted=r.isFileDrag(t)?2:1),1!=cur.uploadDragStarted&&r.dropbox[e]?(setTimeout((function(){clearTimeout(r.dragTimer[e]),delete r.dragTimer[e]}),0),r.options[e].onDragEnter&&r.options[e].onDragEnter(t),show(r.dropbox[e]),cancelEvent(t)):cancelEvent(t)},dragOut:function(e,t){if(1!=cur.uploadDragStarted&&r.dropbox[e]){r.dragTimer[e]&&(clearTimeout(r.dragTimer[e]),delete r.dragTimer[e]);var o=function(){var t=r.options[e],o=r.dropbox[e];t.visibleDropbox||hide(o),t.onDragOut&&t.onDragOut(),removeClass(o,"dropbox_over")};!t.clientX&&!t.clientY?o():r.dragTimer[e]=setTimeout(o,100),cancelEvent(t)}else cancelEvent(t)},dragOver:function(e,t){if(1!=cur.uploadDragStarted&&r.dropbox[e]){var o=r.insideDropbox(e,t);t.dataTransfer&&"copy"!==t.dataTransfer.dropEffect&&(t.dataTransfer.dropEffect=o?"copy":"none"),toggleClass(r.dropbox[e],"dropbox_over",o),cancelEvent(t)}else cancelEvent(t)},drop:function(e){return each(r.dropbox,(function(t,o){o&&(r.insideDropbox(t,e)&&r.onFileApiSend(t,e.dataTransfer.files),r.options[t].visibleDropbox||hide(o),r.options[t].onDrop&&r.options[t].onDrop(),removeClass(o,"dropbox_over"))})),delete cur.uploadDragStarted,cancelEvent(e),!1},insideDropbox:function(e,t){for(var o=t.target;o.parentNode;){if(o==r.dropbox[e])return!0;o=o.parentNode}return!1},isSomethingUploading:function(e){var t=r.options[e];return!!t&&(!(!t.filesQueue||!t.filesQueue.length)||(!(!t.xhr||4===t.xhr.readyState||0===t.xhr.readyState)||(!(!t.uploadOptionsXhr||4===t.uploadOptionsXhr.readyState||0===t.uploadOptionsXhr.readyState)||!!(t.chunked&&t.chunkedUpload&&t.chunkedUpload.activeRequests.length))))},flashCallbacks:function(){return{onUploadStart:r.onUploadStart,onUploadProgress:r.onUploadProgress,onUploadSuccess:r.onUploadComplete,onUploadComplete:r.onUploadCompleteAll,onUploadError:r.onUploadError,onDebug:r.onDebug,onMouseDown:r.buttonDown,onMouseUp:r.buttonUp,onMouseOver:r.buttonOver,onMouseOut:r.buttonOut,onSelectClick:r.onSelectClick}},sendUploadStat:function(e,t){var o=r.options[e],i=r.vars[e];if(!o.signed&&o.error_hash){var a=extend({act:"stat",mid:i.mid,oid:i.oid,gid:i.gid,aid:i.aid,server:o.server,error:o.error,hash:o.error_hash},t);ajax.post("upload_fails.php",a)}}}}}]);try{stManager.done("dist/f58ec69ce22b9ab06724ed2c0702eee6.cc3d21e1d07f61af78fa.js")}catch(e){}