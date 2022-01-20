import "./share.css";
import { PermMedia, Label, Room, EmojiEmotions } from "@material-ui/icons"

export default function Share() {
    return (
        <div className="share">
            <div className="shareWrapper">
                <div className="shareTop">
                    <input placeholder="Compose message here" className="shareInput"/>
                </div>
                
                <div className="shareBottom"></div>
                <button className="shareButton">Share</button>
            </div>
        </div>
    );
}