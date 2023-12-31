import{B as A,A as F,_ as J,P as W,T as V,c as O,a as T,S as L}from"./copy-to-clipboard.5b139da3.js";import{d as b,u as I,c as B,o as _,a as g,w as P,b as s,t as M,n as u,e as y,f as w,g as U,h as R,r as v,i as G,j as z,k as E,F as N,l as j,m as q,p as x,q as K}from"./index.e10ba36f.js";import{_ as S}from"./plugin-vue_export-helper.21dcd24c.js";var Q="/assets/setting-icon.209d1eb3.svg";const X="_info_ds0ox_1";var Y={info:X};const Z=b({__name:"ChainSelect",setup(p){const e=I(),o=B(()=>{var l;return(l=e.chain)==null?void 0:l.name});return(l,a)=>(_(),g(A,null,{default:P(()=>[s("div",{class:u(l.$style.info)},[s("h3",null,M(o.value||"Chain"),1)],2),s("div",{class:u(l.$style.arrow)},[y(F,{color:"#D7D7D7"})],2)]),_:1}))}}),ee={$style:Y};var le=S(Z,[["__cssModules",ee]]);const se="_header_1syas_1",ae="_control_1syas_8";var te={header:se,control:ae};const oe=s("img",{src:J,alt:"logo"},null,-1),re=[oe],ne=s("img",{src:Q,alt:"chain-icon"},null,-1),ue=b({__name:"Header",setup(p){const e=I();return(o,l)=>(_(),w("header",{class:u(o.$style.header)},[s("div",{class:u(o.$style.logo)},re,2),s("div",{class:u(o.$style.control)},[y(le,{onClick:l[0]||(l[0]=a=>U(e).setPopup("select-chain"))}),y(A,{onClick:l[1]||(l[1]=a=>U(e).setPopup("edit-user-info"))},{default:P(()=>[ne]),_:1})],2)],2))}}),de={$style:te};var ie=S(ue,[["__cssModules",de]]);const ce=b({__name:"AuthPopup",setup(p){const e=R(),o=v(""),l=B(()=>e.error),a=async()=>{await e.auth(o.value)};return(c,m)=>(_(),g(W,{"is-logo":!0,"text-button":"Unlock",onButtonClick:a},{default:P(()=>[y(V,{modelValue:o.value,"onUpdate:modelValue":m[0]||(m[0]=i=>o.value=i),label:"Enter access key",placeholder:"Access key",error:l.value},null,8,["modelValue","error"])]),_:1}))}}),pe="_body_1dwfe_1",ve="_editing_1dwfe_6";var _e={body:pe,editing:ve};const me=b({__name:"UserInfoPopup",props:{isEditing:Boolean},setup(p){var t,k,h;const e=R(),o=I(),l={private_key:"",wallet_address:"",inch_api_swap_key:"",inch_api_key:""},a=v(localStorage.private_key||""),c=v(((t=e.me)==null?void 0:t.wallet_address)||""),m=v(((k=e.me)==null?void 0:k.inch_api_swap_key)||""),i=v(((h=e.me)==null?void 0:h.inch_api_key)||""),n=v(l),f=()=>(n.value.private_key="",n.value.wallet_address="",n.value.inch_api_swap_key="",n.value.inch_api_key="",a.value||(n.value.private_key="Please, enter Private key"),c.value||(n.value.wallet_address="Please, enter Wallet address"),m.value||(n.value.inch_api_swap_key="Please, enter 1Inch api swap key"),i.value||(n.value.inch_api_key="Please, enter 1Inch api key"),!(n.value.private_key||n.value.wallet_address||n.value.inch_api_swap_key||n.value.inch_api_key)),C=async()=>{f()&&(await e.saveMeData({private_key:a.value,wallet_address:c.value,inch_api_swap_key:m.value,inch_api_key:i.value}),o.setPopup(""))};return($,r)=>(_(),g(W,{title:p.isEditing&&"Edit user info","is-logo":!p.isEditing,"text-button":p.isEditing?"save settings":"add user info",onButtonClick:C},{default:P(()=>[s("div",{class:u([$.$style.body,{[$.$style.editing]:p.isEditing}])},[y(V,{modelValue:a.value,"onUpdate:modelValue":r[0]||(r[0]=d=>a.value=d),label:"Enter private key",placeholder:"Private key",secret:!0,error:n.value.private_key},null,8,["modelValue","error"]),y(V,{modelValue:c.value,"onUpdate:modelValue":r[1]||(r[1]=d=>c.value=d),label:"Enter wallet address",placeholder:"Wallet address",error:n.value.wallet_address},null,8,["modelValue","error"]),y(V,{modelValue:i.value,"onUpdate:modelValue":r[2]||(r[2]=d=>i.value=d),label:"Enter 1Inch api key",placeholder:"1Inch api key",error:n.value.inch_api_key},null,8,["modelValue","error"]),y(V,{modelValue:m.value,"onUpdate:modelValue":r[3]||(r[3]=d=>m.value=d),label:"Enter 1Inch swap api key",placeholder:"1Inch swap api key",error:n.value.inch_api_swap_key},null,8,["modelValue","error"])],2)]),_:1},8,["title","is-logo","text-button"]))}}),ye={$style:_e};var H=S(me,[["__cssModules",ye]]);const $e="_item_1tjpe_1",fe="_address_1tjpe_22";var ge={item:$e,address:fe};const he=s("img",{src:T,alt:"copy"},null,-1),ke=b({__name:"AddressItem",props:{name:String,address:String},setup(p){const e=o=>{O(o)};return(o,l)=>(_(),w("div",{class:u(o.$style.item)},[s("h3",null,M(p.name),1),s("div",{class:u(o.$style.address)},[s("span",null,M(p.address),1),y(A,{type:"mini",onClick:l[0]||(l[0]=a=>e(p.address))},{default:P(()=>[he]),_:1})],2)],2))}}),Ve={$style:ge};var be=S(ke,[["__cssModules",Ve]]);const Se="_body_le479_1",Ce="_scroll_le479_7",we="_bodyWrapper_le479_22",Pe="_empty_le479_26",Me="_divider_le479_34",Ie="_control_le479_42";var We={body:Se,scroll:Ce,bodyWrapper:we,empty:Pe,divider:Me,control:Ie};const Be=b({__name:"AddressesPopup",setup(p){const e=G(),o=v(null),l=v(!0),a=v(""),c=v(""),m=v(""),i=v({name:"",address:""}),n=B(()=>a.value?e.addresses.filter(t=>t.name.toLowerCase().includes(a.value.toLowerCase())):e.addresses);z(()=>{const t=o.value.clientHeight;o.value.scrollHeight<=t&&(l.value=!1)});const f=()=>(i.value.name="",i.value.address="",c.value||(i.value.name="Please, enter name"),m.value||(i.value.address="Please, enter address"),!(i.value.name||i.value.address)),C=async()=>{f()&&(await e.addAddress({name:c.value,address:m.value}),c.value="",m.value="")};return(t,k)=>(_(),g(W,{"text-button":"Add address",title:"Addresses",onButtonClick:C},{default:P(()=>[y(L,{modelValue:a.value,"onUpdate:modelValue":k[0]||(k[0]=h=>a.value=h),type:"popup"},null,8,["modelValue"]),s("div",{class:u(t.$style.divider)},null,2),s("div",{ref_key:"scroll",ref:o,class:u([t.$style.body,{[t.$style.scroll]:l.value}])},[s("div",{class:u(t.$style.bodyWrapper)},[(_(!0),w(N,null,E(n.value,h=>(_(),g(be,{key:h.id,name:h.name,address:h.wallet_address},null,8,["name","address"]))),128)),n.value.length?j("",!0):(_(),w("p",{key:0,class:u(t.$style.empty)},"No addresses added",2))],2)],2),s("div",{class:u(t.$style.divider)},null,2),s("div",{class:u(t.$style.control)},[y(V,{modelValue:c.value,"onUpdate:modelValue":k[1]||(k[1]=h=>c.value=h),type:"md",placeholder:"Name",error:i.value.name},null,8,["modelValue","error"]),y(V,{modelValue:m.value,"onUpdate:modelValue":k[2]||(k[2]=h=>m.value=h),type:"md",placeholder:"Address",error:i.value.address},null,8,["modelValue","error"])],2)]),_:1}))}}),Ue={$style:We};var Ae=S(Be,[["__cssModules",Ue]]),Ee="/assets/select-border.2469c53b.svg",Ne="/assets/select-circle.34678bb9.svg";const je="_item_1gu5y_1",De="_itemWrapper_1gu5y_22",He="_meta_1gu5y_40",Le="_ratio_1gu5y_58",Re="_selected_1gu5y_71";var ze={item:je,itemWrapper:De,meta:He,ratio:Le,selected:Re};const Fe=s("img",{src:Ee,alt:""},null,-1),Je=s("img",{src:Ne,alt:""},null,-1),Oe=[Fe,Je],Te=b({__name:"SelectChainItem",props:{selected:Boolean,name:String,monet:String},setup(p){return(e,o)=>(_(),w("div",{class:u([e.$style.item,{[e.$style.selected]:p.selected}])},[s("div",{class:u(e.$style.itemWrapper)},[s("div",{class:u(e.$style.meta)},[s("h3",null,M(p.name),1),s("p",null,M(p.monet),1)],2),s("div",{class:u(e.$style.ratio)},Oe,2)],2)],2))}}),Ge={$style:ze};var qe=S(Te,[["__cssModules",Ge]]);const xe="_body_1ctxo_1",Ke="_scroll_1ctxo_8",Qe="_bodyWrapper_1ctxo_23",Xe="_empty_1ctxo_28",Ye="_divider_1ctxo_36",Ze="_control_1ctxo_44",el="_controlRow_1ctxo_51";var ll={body:xe,scroll:Ke,bodyWrapper:Qe,empty:Xe,divider:Ye,control:Ze,controlRow:el};const sl=b({__name:"SelectChainPopup",setup(p){const e=I(),o=B(()=>e.chains),l=v(e.chain||{}),a=v(e.rpc),c=v(e.address),m=v(e.gas_limit),i=v(e.decimals),n=v(e.gas_factor),f=v({}),C=v(!0),t=v({rpc:"",address:"",decimals:"",gas_limit:"",gas_factor:""});q(l,()=>{const r=(localStorage.chains?JSON.parse(localStorage.chains):[]).find(d=>d.id===l.value.id);a.value=r?r.rpc:"",c.value=r?r.address:"",i.value=r?+r.decimals:"",m.value=r?+r.gas_limit:"",n.value=r?+r.gas_factor:""},{deep:!0});const k=()=>{if(h()){e.rpc=a.value,e.address=c.value,e.decimals=+i.value,e.gas_limit=+m.value,e.gas_factor=+n.value,e.selectChain(l.value.id);const $=localStorage.chains?JSON.parse(localStorage.chains):[],r=$.findIndex(D=>D.id===l.value.id),d={id:l.value.id,rpc:a.value,address:c.value,decimals:i.value,gas_limit:m.value,gas_factor:n.value};r>-1?$[r]=d:$.push(d),localStorage.chains=JSON.stringify($),e.setPopup("")}},h=()=>(t.value.rpc="",t.value.address="",t.value.gas_limit="",t.value.decimals="",t.value.gas_factor="",a.value||(t.value.rpc="Please, enter RPC"),c.value||(t.value.address="Please, enter address"),m.value||(t.value.gas_limit="Please, enter gas limit"),i.value||(t.value.decimals="Please, enter decimals"),n.value||(t.value.gas_factor="Please, enter gas factor"),!(t.value.rpc||t.value.address||t.value.gas_limit||t.value.decimals||t.value.gas_factor));return z(()=>{if(f.value){const $=f.value.clientHeight;f.value.scrollHeight<=$&&(C.value=!1)}}),($,r)=>(_(),g(W,{"text-button":"Select chain",title:"Chains","disabled-close":!U(e).chain,onButtonClick:k},{default:P(()=>[y(L,{type:"popup"}),s("div",{class:u($.$style.divider)},null,2),s("div",{ref_key:"scroll",ref:f,class:u([$.$style.body,{[$.$style.scroll]:C.value}])},[s("div",{class:u($.$style.bodyWrapper)},[(_(!0),w(N,null,E(o.value,d=>(_(),g(qe,{key:d.id,name:d.name,monet:d.native_token_symbol,selected:d.id===l.value.id,onClick:D=>l.value=d},null,8,["name","monet","selected","onClick"]))),128)),j("",!0)],2)],2),s("div",{class:u($.$style.divider)},null,2),s("div",{class:u($.$style.control)},[y(V,{modelValue:a.value,"onUpdate:modelValue":r[0]||(r[0]=d=>a.value=d),error:t.value.rpc,type:"md",placeholder:"RPC"},null,8,["modelValue","error"]),y(V,{modelValue:c.value,"onUpdate:modelValue":r[1]||(r[1]=d=>c.value=d),error:t.value.address,type:"md",placeholder:"Base token address"},null,8,["modelValue","error"]),s("div",{class:u($.$style.controlRow)},[y(V,{modelValue:i.value,"onUpdate:modelValue":r[2]||(r[2]=d=>i.value=d),error:t.value.decimals,type:"md",placeholder:"Decimals"},null,8,["modelValue","error"]),y(V,{modelValue:m.value,"onUpdate:modelValue":r[3]||(r[3]=d=>m.value=d),error:t.value.gas_limit,type:"md",placeholder:"Gas limit"},null,8,["modelValue","error"]),y(V,{modelValue:n.value,"onUpdate:modelValue":r[4]||(r[4]=d=>n.value=d),error:t.value.gas_factor,type:"md",placeholder:"Gas factor"},null,8,["modelValue","error"])],2)],2)]),_:1},8,["disabled-close"]))}}),al={$style:ll};var tl=S(sl,[["__cssModules",al]]);const ol="_item_1j8fv_1",rl="_itemWrapper_1j8fv_6",nl="_selected_1j8fv_44",ul="_input_1j8fv_60";var dl={item:ol,itemWrapper:rl,selected:nl,input:ul};const il=["value"],cl=b({__name:"SlippageSelect",props:{type:String,label:String,selected:Boolean,modelValue:String},emits:["update:modelValue"],setup(p,{emit:e}){const o=e,l=a=>{o("update:modelValue",a.target.value)};return(a,c)=>(_(),w("div",{class:u([a.$style.item,a.$style[p.type],{[a.$style.selected]:p.selected}])},[s("div",{class:u(a.$style.itemWrapper)},[s("h3",null,M(p.label),1),s("input",{value:p.modelValue,type:"number",placeholder:"0.00%",onInput:l},null,40,il)],2)],2))}}),pl={$style:dl};var vl=S(cl,[["__cssModules",pl]]);const _l="_body_1acxj_1";var ml={body:_l};const yl=b({__name:"SlippagePopup",setup(p){const e=x(),o=I(),l=v([{id:0,value:.1},{id:1,value:.3},{id:2,value:.5},{id:3,value:"Custom"}]),a=v(l.value.find(i=>i.value===e.slippage)?e.slippage:"Custom"),c=v(e.slippage),m=()=>{e.slippage=a.value==="Custom"?c:a,o.setPopup("")};return(i,n)=>(_(),g(W,{title:"Slippage settings","text-button":"Save settings",onButtonClick:m},{default:P(()=>[s("div",{class:u(i.$style.body)},[(_(!0),w(N,null,E(l.value,f=>(_(),g(vl,{modelValue:c.value,"onUpdate:modelValue":n[0]||(n[0]=C=>c.value=C),selected:a.value===f.value,label:f.value==="Custom"?f.value:`${f.value}%`,type:f.value==="Custom"&&"input",onClick:C=>a.value=f.value},null,8,["modelValue","selected","label","type","onClick"]))),256))],2)]),_:1}))}}),$l={$style:ml};var fl=S(yl,[["__cssModules",$l]]);const gl="_layout_1rdzx_1",hl="_main_1rdzx_7";var kl={layout:gl,main:hl};const Vl=s("footer",null,null,-1),bl=b({__name:"MainLayout",setup(p){const e=I(),o=B(()=>e.popup);return(l,a)=>{const c=K("router-view");return _(),w("div",{class:u(l.$style.layout)},[y(ie),s("main",{class:u(l.$style.main)},[y(c)],2),Vl,o.value==="auth"?(_(),g(ce,{key:0})):o.value==="set-user-info"?(_(),g(H,{key:1})):o.value==="edit-user-info"?(_(),g(H,{key:2,"is-editing":!0})):o.value==="addresses"?(_(),g(Ae,{key:3})):o.value==="select-chain"?(_(),g(tl,{key:4})):o.value==="slippage"?(_(),g(fl,{key:5})):j("",!0)],2)}}}),Sl={$style:kl};var Ml=S(bl,[["__cssModules",Sl]]);export{Ml as default};