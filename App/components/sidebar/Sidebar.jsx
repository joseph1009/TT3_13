import "./sidebar.css";
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
                    <span className="sidebarListItemText">Home</span>
                    </li>
                    <li className="sidebarListItem">
                        <span className="sidebarListItemText">Profile</span>
                    </li>
                </ul>
            </div>
        </div>
    );
}