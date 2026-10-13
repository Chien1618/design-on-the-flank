import * as React from "react"
import { addPropertyControls, ControlType } from "framer"

interface Props {
    title?: string
    body?: string
    showBody?: boolean
    background?: string
    textColor?: string
    padding?: number
    radius?: number
    style?: React.CSSProperties
}

const defaults = {
    title: "Your next idea starts here",
    body: "Change this text, the colors, and the spacing in the Properties panel.",
    showBody: true,
    background: "#F1F0EB",
    textColor: "#20201E",
    padding: 24,
    radius: 16,
}

/**
 * @framerSupportedLayoutWidth any
 * @framerSupportedLayoutHeight auto
 * @framerIntrinsicWidth 360
 * @framerIntrinsicHeight 200
 */
export default function FlankCard(props: Props) {
    const {
        title = defaults.title,
        body = defaults.body,
        showBody = defaults.showBody,
        background = defaults.background,
        textColor = defaults.textColor,
        padding = defaults.padding,
        radius = defaults.radius,
        style,
    } = props

    return (
        <div
            style={{
                width: "100%",
                boxSizing: "border-box",
                display: "flex",
                flexDirection: "column",
                gap: 12,
                background,
                color: textColor,
                padding,
                borderRadius: radius,
                fontFamily: "system-ui, sans-serif",
                overflowWrap: "anywhere",
                ...style,
            }}
        >
            <h2 style={{ margin: 0, fontSize: 24, lineHeight: 1.2 }}>{title}</h2>
            {showBody && (
                <p style={{ margin: 0, fontSize: 16, lineHeight: 1.5 }}>{body}</p>
            )}
        </div>
    )
}

FlankCard.defaultProps = defaults

addPropertyControls(FlankCard, {
    title: { type: ControlType.String, title: "Title", defaultValue: defaults.title },
    showBody: { type: ControlType.Boolean, title: "Show text", defaultValue: defaults.showBody },
    body: {
        type: ControlType.String,
        title: "Text",
        displayTextArea: true,
        defaultValue: defaults.body,
        hidden: (props) => props.showBody === false,
    },
    background: { type: ControlType.Color, title: "Background", defaultValue: defaults.background },
    textColor: { type: ControlType.Color, title: "Text color", defaultValue: defaults.textColor },
    padding: { type: ControlType.Number, title: "Padding", min: 0, max: 100, step: 1, unit: "px", defaultValue: defaults.padding },
    radius: { type: ControlType.Number, title: "Corners", min: 0, max: 100, step: 1, unit: "px", defaultValue: defaults.radius },
})
