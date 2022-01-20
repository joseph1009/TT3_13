﻿import "./sidebar.css";
import {
    Home,
    Person,
} from "@material-ui/icons";


export default function Sidebar() {
    return (
        <div className="sidebar">
            <div className="sidebarWrapper">
                <ul className="sidebarList">
                    <li className="sidebarListItem">
                    <Home className="sidebarIcon" />
                    <span className="sidebarListItemText">Feed</span>
                   </li>
                </ul>
            </div>
        </div>
    );
}