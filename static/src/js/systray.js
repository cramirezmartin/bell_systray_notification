/** @odoo-module **/
import { registry } from "@web/core/registry";
import { useService } from "@web/core/utils/hooks";
import { Component } from "@odoo/owl";

class bellSystrayNotificationsIcon extends Component { 
    setup() {
        super.setup(...arguments);
        this.action = useService("action"); 
        this.rpc = useService("rpc");

        const onwillstart = async () => {return await this.rpc("/get_bell_systray_notification_counter", {});};
        const showNotifications = async () => {await this.rpc("/show_bell_systray_notification", {});};
        this.showNotifications = showNotifications;
        
        setInterval(function(){
            onwillstart().then(function (result) {
                let badge = document.getElementById('bell_systray_notification_counter_badge');
                if(result == 0) result = '';
                if(badge != null) badge.innerHTML = result;
            });
        }, 60000);

        onwillstart().then(function (result) {
            let badge = document.getElementById('bell_systray_notification_counter_badge');
            if(result == 0) result = '';
            if(badge != null) badge.innerHTML = result;;
        });
    }

    _onClickBellSystrayNotificationIcon() {
        this.showNotifications().then(function (result) {
            let badge = document.getElementById('bell_systray_notification_counter_badge');
            if(badge != null) badge.innerHTML = '';
        });
    }
}

bellSystrayNotificationsIcon.template = "bell_systray_notification_icon";
export const systrayBellNotificationItem = { Component: bellSystrayNotificationsIcon,};
registry.category("systray").add("bellSystrayNotificationsIcon", systrayBellNotificationItem, { sequence: 1 });
