from discord import PermissionOverwrite

_staff_team_permissive = PermissionOverwrite(
    create_instant_invite=False,
    manage_channels=True,
    add_reactions=True,
    priority_speaker=False,
    stream=True,
    read_messages=True,
    view_channel=True,
    send_messages=True,
    send_tts_messages=False,
    manage_messages=True,
    embed_links=True,
    attach_files=True,
    read_message_history=True,
    mention_everyone=True,
    external_emojis=True,
    connect=True,
    speak=True,
    mute_members=True,
    deafen_members=True,
    move_members=True,
    use_voice_activation=True,
    manage_permissions=True,
    manage_webhooks=False,
)

_no_permissions = PermissionOverwrite(
    create_instant_invite=False,
    manage_channels=False,
    add_reactions=False,
    priority_speaker=False,
    stream=False,
    read_messages=False,
    view_channel=False,
    send_messages=False,
    send_tts_messages=False,
    manage_messages=False,
    embed_links=False,
    attach_files=False,
    read_message_history=False,
    mention_everyone=False,
    external_emojis=False,
    connect=False,
    speak=False,
    mute_members=False,
    deafen_members=False,
    move_members=False,
    use_voice_activation=False,
    manage_permissions=False,
    manage_webhooks=False,
)

lockdown_permissions = PermissionOverwrite(
    create_instant_invite=False,
    manage_channels=False,
    add_reactions=False,
    priority_speaker=False,
    stream=True,
    read_messages=True,
    view_channel=True,
    send_messages=False,
    send_tts_messages=False,
    manage_messages=False,
    embed_links=False,
    attach_files=False,
    read_message_history=True,
    mention_everyone=False,
    external_emojis=False,
    connect=False,
    speak=True,
    mute_members=False,
    deafen_members=False,
    move_members=False,
    use_voice_activation=True,
    manage_permissions=False,
    manage_webhooks=False,
)

_read_only_permissions = PermissionOverwrite(
    create_instant_invite=False,
    manage_channels=False,
    add_reactions=False,
    priority_speaker=False,
    stream=False,
    read_messages=True,
    view_channel=True,
    send_messages=False,
    send_tts_messages=False,
    manage_messages=False,
    embed_links=False,
    attach_files=False,
    read_message_history=True,
    mention_everyone=False,
    external_emojis=False,
    connect=False,
    speak=False,
    mute_members=False,
    deafen_members=False,
    move_members=False,
    use_voice_activation=False,
    manage_permissions=False,
    manage_webhooks=False,
)

_muted_read_only_permissions = PermissionOverwrite(
    create_instant_invite=False,
    manage_channels=False,
    add_reactions=False,
    priority_speaker=False,
    stream=False,
    send_messages=False,
    send_tts_messages=False,
    manage_messages=False,
    embed_links=False,
    attach_files=False,
    read_message_history=True,
    mention_everyone=False,
    external_emojis=False,
    connect=False,
    speak=False,
    mute_members=False,
    deafen_members=False,
    move_members=False,
    use_voice_activation=False,
    manage_permissions=False,
    manage_webhooks=False,
)

_moderation_send_all_and_read_all_permission = PermissionOverwrite(
    create_instant_invite=False,
    manage_channels=False,
    add_reactions=True,
    priority_speaker=False,
    stream=True,
    read_messages=True,
    view_channel=True,
    send_messages=True,
    send_tts_messages=False,
    manage_messages=False,
    embed_links=True,
    attach_files=True,
    read_message_history=True,
    mention_everyone=True,
    external_emojis=True,
    connect=True,
    speak=True,
    mute_members=False,
    deafen_members=False,
    move_members=False,
    use_voice_activation=True,
    manage_permissions=False,
    manage_webhooks=False,
)

_moderation_privileged_permissions = PermissionOverwrite(
    create_instant_invite=False,
    manage_channels=False,
    add_reactions=True,
    priority_speaker=False,
    stream=True,
    read_messages=True,
    view_channel=True,
    send_messages=True,
    send_tts_messages=False,
    manage_messages=False,
    embed_links=True,
    attach_files=True,
    read_message_history=True,
    mention_everyone=True,
    external_emojis=True,
    connect=True,
    speak=True,
    mute_members=True,
    deafen_members=True,
    move_members=True,
    use_voice_activation=True,
    manage_permissions=False,
    manage_webhooks=False,
)

_staff_team_read_only = PermissionOverwrite(
    create_instant_invite=False,
    manage_channels=False,
    add_reactions=True,
    priority_speaker=False,
    stream=False,
    read_messages=True,
    view_channel=True,
    send_messages=False,
    send_tts_messages=False,
    manage_messages=False,
    embed_links=False,
    attach_files=False,
    read_message_history=True,
    mention_everyone=False,
    external_emojis=True,
    connect=False,
    speak=False,
    mute_members=False,
    deafen_members=False,
    move_members=False,
    use_voice_activation=False,
    manage_permissions=False,
    manage_webhooks=False,
)

_read_and_send_only = PermissionOverwrite(
    create_instant_invite=False,
    manage_channels=False,
    add_reactions=False,
    priority_speaker=False,
    stream=False,
    read_messages=True,
    view_channel=True,
    send_messages=True,
    send_tts_messages=False,
    manage_messages=False,
    embed_links=False,
    attach_files=False,
    read_message_history=True,
    mention_everyone=False,
    external_emojis=False,
    connect=False,
    speak=False,
    mute_members=False,
    deafen_members=False,
    move_members=False,
    use_voice_activation=False,
    manage_permissions=False,
    manage_webhooks=False,
)

_citizen_general_perms = PermissionOverwrite(
    create_instant_invite=False,
    manage_channels=False,
    add_reactions=True,
    priority_speaker=False,
    stream=True,
    read_messages=True,
    view_channel=True,
    send_messages=True,
    send_tts_messages=False,
    manage_messages=False,
    embed_links=True,
    attach_files=True,
    read_message_history=True,
    mention_everyone=False,
    external_emojis=True,
    connect=True,
    speak=True,
    mute_members=False,
    deafen_members=False,
    move_members=False,
    use_voice_activation=True,
    manage_permissions=False,
    manage_webhooks=False,
)

lockdown_citizen_general_perms = PermissionOverwrite(
    create_instant_invite=False,
    manage_channels=False,
    add_reactions=False,
    priority_speaker=False,
    stream=True,
    read_messages=True,
    view_channel=True,
    send_messages=False,
    send_tts_messages=False,
    manage_messages=False,
    embed_links=False,
    attach_files=False,
    read_message_history=True,
    mention_everyone=False,
    external_emojis=True,
    connect=False,
    speak=True,
    mute_members=False,
    deafen_members=False,
    move_members=False,
    use_voice_activation=True,
    manage_permissions=False,
    manage_webhooks=False,
)

_moderator_general_perms = PermissionOverwrite(
    create_instant_invite=False,
    manage_channels=False,
    add_reactions=True,
    priority_speaker=True,
    stream=True,
    read_messages=True,
    view_channel=True,
    send_messages=True,
    send_tts_messages=False,
    manage_messages=True,
    embed_links=True,
    attach_files=True,
    read_message_history=True,
    mention_everyone=False,
    external_emojis=True,
    connect=True,
    speak=True,
    mute_members=True,
    deafen_members=True,
    move_members=True,
    use_voice_activation=True,
    manage_permissions=False,
    manage_webhooks=False,
)


_senior_mod_general_perms = PermissionOverwrite(
    create_instant_invite=False,
    manage_channels=False,
    add_reactions=True,
    priority_speaker=True,
    stream=True,
    read_messages=True,
    view_channel=True,
    send_messages=True,
    send_tts_messages=False,
    manage_messages=True,
    embed_links=True,
    attach_files=True,
    read_message_history=True,
    mention_everyone=True,
    external_emojis=True,
    connect=True,
    speak=True,
    mute_members=True,
    deafen_members=True,
    move_members=True,
    use_voice_activation=True,
    manage_permissions=False,
    manage_webhooks=False,
)

_moderator_log_permissions = PermissionOverwrite(
    create_instant_invite=False,
    manage_channels=False,
    add_reactions=False,
    priority_speaker=False,
    stream=False,
    read_messages=True,
    view_channel=True,
    send_messages=False,
    send_tts_messages=False,
    manage_messages=False,
    embed_links=True,
    attach_files=True,
    read_message_history=True,
    mention_everyone=False,
    external_emojis=False,
    connect=False,
    speak=False,
    mute_members=False,
    deafen_members=False,
    move_members=False,
    use_voice_activation=False,
    manage_permissions=False,
    manage_webhooks=False,
)

_senior_mod_log_perms = PermissionOverwrite(
    create_instant_invite=False,
    manage_channels=False,
    add_reactions=False,
    priority_speaker=False,
    stream=False,
    read_messages=True,
    view_channel=True,
    send_messages=False,
    send_tts_messages=False,
    manage_messages=True,
    embed_links=True,
    attach_files=True,
    read_message_history=True,
    mention_everyone=False,
    external_emojis=False,
    connect=False,
    speak=False,
    mute_members=False,
    deafen_members=False,
    move_members=False,
    use_voice_activation=False,
    manage_permissions=False,
    manage_webhooks=False,
)

_debate_member_perms = PermissionOverwrite(
    create_instant_invite=False,
    manage_channels=False,
    add_reactions=True,
    priority_speaker=False,
    stream=False,
    read_messages=True,
    view_channel=True,
    send_messages=True,
    send_tts_messages=False,
    manage_messages=False,
    embed_links=False,
    attach_files=False,
    read_message_history=True,
    mention_everyone=False,
    external_emojis=False,
    connect=True,
    speak=True,
    mute_members=False,
    deafen_members=False,
    move_members=False,
    use_voice_activation=True,
    manage_permissions=False,
    manage_webhooks=False,
)

lockdown_debate_member_perms = PermissionOverwrite(
    create_instant_invite=False,
    manage_channels=False,
    add_reactions=True,
    priority_speaker=False,
    stream=False,
    read_messages=True,
    view_channel=True,
    send_messages=False,
    send_tts_messages=False,
    manage_messages=False,
    embed_links=False,
    attach_files=False,
    read_message_history=True,
    mention_everyone=False,
    external_emojis=False,
    connect=False,
    speak=True,
    mute_members=False,
    deafen_members=False,
    move_members=False,
    use_voice_activation=True,
    manage_permissions=False,
    manage_webhooks=False,
)

_debate_tc_citizen_permissions = PermissionOverwrite(
    create_instant_invite=False,
    manage_channels=False,
    add_reactions=True,
    priority_speaker=False,
    stream=False,
    read_messages=False,
    view_channel=False,
    send_messages=True,
    send_tts_messages=False,
    manage_messages=False,
    embed_links=True,
    attach_files=True,
    read_message_history=True,
    mention_everyone=False,
    external_emojis=True,
    connect=False,
    speak=False,
    mute_members=False,
    deafen_members=False,
    move_members=False,
    use_voice_activation=False,
    manage_permissions=False,
    manage_webhooks=False,
)

_debate_tc_member_permissions = PermissionOverwrite(
    create_instant_invite=False,
    manage_channels=False,
    add_reactions=True,
    priority_speaker=False,
    stream=False,
    read_messages=False,
    view_channel=False,
    send_messages=True,
    send_tts_messages=False,
    manage_messages=False,
    embed_links=False,
    attach_files=False,
    read_message_history=True,
    mention_everyone=False,
    external_emojis=False,
    connect=False,
    speak=False,
    mute_members=False,
    deafen_members=False,
    move_members=False,
    use_voice_activation=False,
    manage_permissions=False,
    manage_webhooks=False,
)

all_channel_overwrites = {
    "information": {
        "role_warden": _staff_team_permissive,
        "role_director": PermissionOverwrite(
            create_instant_invite=False,
            manage_channels=False,
            add_reactions=False,
            priority_speaker=False,
            stream=False,
            read_messages=True,
            view_channel=True,
            send_messages=False,
            send_tts_messages=False,
            manage_messages=True,
            embed_links=True,
            attach_files=True,
            read_message_history=True,
            mention_everyone=True,
            external_emojis=True,
            connect=False,
            speak=False,
            mute_members=False,
            deafen_members=False,
            move_members=False,
            use_voice_activation=False,
            manage_permissions=False,
            manage_webhooks=False,
        ),
        "role_moderator": _read_only_permissions,
        "role_citizen": _read_only_permissions,
        "role_member": _read_only_permissions,
        "role_logs": _no_permissions,
        "role_detained": _read_only_permissions,
        "role_muted": _read_only_permissions,
        "role_super_muted": _no_permissions,
        "role_everyone": PermissionOverwrite(
            create_instant_invite=False,
            manage_channels=False,
            add_reactions=False,
            priority_speaker=False,
            stream=False,
            read_messages=True,
            view_channel=True,
            send_messages=False,
            send_tts_messages=False,
            manage_messages=False,
            embed_links=False,
            attach_files=False,
            read_message_history=True,
            mention_everyone=False,
            external_emojis=False,
            connect=False,
            speak=False,
            mute_members=False,
            deafen_members=False,
            move_members=False,
            use_voice_activation=True,
            manage_permissions=False,
            manage_webhooks=False,
        ),
    },
    "verification": {
        "role_warden": _staff_team_permissive,
        "role_director": _staff_team_read_only,
        "role_moderator": _no_permissions,
        "role_citizen": _no_permissions,
        "role_member": _no_permissions,
        "role_logs": _no_permissions,
        "role_detained": _no_permissions,
        "role_muted": _no_permissions,
        "role_super_muted": _no_permissions,
        "role_everyone": _read_only_permissions,
    },
    "community_updates": {
        "role_warden": _staff_team_permissive,
        "role_director": _staff_team_read_only,
        "role_moderator": _no_permissions,
        "role_citizen": _no_permissions,
        "role_member": _no_permissions,
        "role_logs": _no_permissions,
        "role_detained": _no_permissions,
        "role_muted": _no_permissions,
        "role_super_muted": _no_permissions,
        "role_everyone": _no_permissions,
    },
    "moderation": {
        "role_warden": _staff_team_permissive,
        "role_director": _moderation_privileged_permissions,
        "role_moderator": _moderation_send_all_and_read_all_permission,
        "role_citizen": _no_permissions,
        "role_member": _no_permissions,
        "role_logs": _no_permissions,
        "role_detained": _no_permissions,
        "role_muted": _no_permissions,
        "role_super_muted": _no_permissions,
        "role_everyone": _no_permissions,
    },
    "director_commands": {
        "role_warden": _staff_team_permissive,
        "role_director": _moderation_privileged_permissions,
        "role_moderator": _no_permissions,
        "role_citizen": _no_permissions,
        "role_member": _no_permissions,
        "role_logs": _no_permissions,
        "role_detained": _no_permissions,
        "role_muted": _no_permissions,
        "role_super_muted": _no_permissions,
        "role_everyone": _no_permissions,
    },
    "isolation": {
        "role_warden": _staff_team_permissive,
        "role_director": _senior_mod_general_perms,
        "role_moderator": _moderator_general_perms,
        "role_citizen": _no_permissions,
        "role_member": _no_permissions,
        "role_logs": _no_permissions,
        "role_detained": _read_and_send_only,
        "role_muted": _no_permissions,
        "role_super_muted": _no_permissions,
        "role_everyone": _no_permissions,
    },
    "interface": {
        "role_warden": _staff_team_permissive,
        "role_director": _senior_mod_general_perms,
        "role_moderator": _read_only_permissions,
        "role_citizen": _read_only_permissions,
        "role_member": _read_only_permissions,
        "role_logs": _no_permissions,
        "role_detained": _no_permissions,
        "role_muted": _read_only_permissions,
        "role_super_muted": _no_permissions,
        "role_everyone": _no_permissions,
    },
    "commands": {
        "role_warden": _staff_team_permissive,
        "role_director": _senior_mod_general_perms,
        "role_moderator": _moderator_general_perms,
        "role_citizen": _citizen_general_perms,
        "role_member": _read_and_send_only,
        "role_logs": _no_permissions,
        "role_detained": _no_permissions,
        "role_muted": _read_only_permissions,
        "role_super_muted": _no_permissions,
        "role_everyone": _no_permissions,
    },
    "community": {
        "role_warden": _staff_team_permissive,
        "role_director": _senior_mod_general_perms,
        "role_moderator": _moderator_general_perms,
        "role_citizen": _citizen_general_perms,
        "role_member": _read_and_send_only,
        "role_logs": _no_permissions,
        "role_detained": _no_permissions,
        "role_muted": _read_only_permissions,
        "role_super_muted": _no_permissions,
        "role_everyone": _no_permissions,
    },
    "debate": {
        "role_warden": _staff_team_permissive,
        "role_director": _senior_mod_general_perms,
        "role_moderator": _moderator_general_perms,
        "role_citizen": _citizen_general_perms,
        "role_member": _debate_member_perms,
        "role_logs": _no_permissions,
        "role_detained": _no_permissions,
        "role_muted": _muted_read_only_permissions,
        "role_super_muted": _no_permissions,
        "role_everyone": _no_permissions,
    },
    "debate-#": {
        "role_warden": _staff_team_permissive,
        "role_director": _senior_mod_general_perms,
        "role_moderator": _moderator_general_perms,
        "role_citizen": _debate_tc_citizen_permissions,
        "role_member": _debate_tc_member_permissions,
        "role_logs": _no_permissions,
        "role_detained": _no_permissions,
        "role_muted": _no_permissions,
        "role_super_muted": _no_permissions,
        "role_everyone": _no_permissions,
    },
    "logs": {
        "role_warden": _staff_team_permissive,
        "role_director": _senior_mod_log_perms,
        "role_moderator": _moderator_log_permissions,
        "role_citizen": _no_permissions,
        "role_member": _no_permissions,
        "role_logs": _read_only_permissions,
        "role_detained": _no_permissions,
        "role_muted": _no_permissions,
        "role_super_muted": _no_permissions,
        "role_everyone": _no_permissions,
    },
}


def generate_overwrite(ctx, roles, channel: str):
    """
    Parameters
    ----------
    ctx: discord context
    roles: a dict of roles pulled from db
    channel: name of any GuildChannel

    Returns
    -------
    A dict of roles and their overwrites for a specific channel
    """
    overwrites = all_channel_overwrites[channel]
    return {
        roles["role_warden"]: overwrites["role_warden"],
        roles["role_director"]: overwrites["role_director"],
        roles["role_moderator"]: overwrites["role_moderator"],
        roles["role_citizen"]: overwrites["role_citizen"],
        roles["role_member"]: overwrites["role_member"],
        roles["role_logs"]: overwrites["role_logs"],
        roles["role_detained"]: overwrites["role_detained"],
        roles["role_muted"]: overwrites["role_muted"],
        roles["role_super_muted"]: overwrites["role_super_muted"],
        ctx.guild.default_role: overwrites["role_everyone"],
    }
